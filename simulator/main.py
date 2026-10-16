from datetime import datetime, timezone
import json
import random
import time

from mqtt_publisher import TelemetryPublisher

MACHINE_ID = "motor-01"

MIN_TEMPERATURE_C = 65.0
MAX_TEMPERATURE_C = 75.0
TEMPERATURE_DELTA_C = 0.3
WARNING_TEMPERATURE_C = 74.0

MIN_VIBRATION_MM_S = 0.08
MAX_VIBRATION_MM_S = 0.20
VIBRATION_DELTA_MM_S = 0.02
WARNING_VIBRATION_MM_S = 0.18

MIN_RPM = 1430
MAX_RPM = 1470
RPM_DELTA = 5

READ_INTERVAL_SECONDS = 1

STATUS_RUNNING = "running"
STATUS_WARNING = "warning"

MQTT_BROKER_HOST = "localhost"
MQTT_BROKER_PORT = 1883
MQTT_CLIENT_ID = f"{MACHINE_ID}-simulator"
MQTT_TOPIC = f"factory/line-1/{MACHINE_ID}/telemetry"
MQTT_AVAILABILITY_TOPIC = f"factory/line-1/{MACHINE_ID}/availability"
MQTT_QOS = 1


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def generate_telemetry(state):
    temperature = state["temperature_c"] + random.uniform(
        -TEMPERATURE_DELTA_C,
        TEMPERATURE_DELTA_C,
    )
    state["temperature_c"] = round(
        clamp(temperature, MIN_TEMPERATURE_C, MAX_TEMPERATURE_C),
        2,
    )

    vibration = state["vibration_mm_s"] + random.uniform(
        -VIBRATION_DELTA_MM_S,
        VIBRATION_DELTA_MM_S,
    )
    state["vibration_mm_s"] = round(
        clamp(vibration, MIN_VIBRATION_MM_S, MAX_VIBRATION_MM_S),
        2,
    )

    rpm = state["rpm"] + random.randint(-RPM_DELTA, RPM_DELTA)
    state["rpm"] = clamp(rpm, MIN_RPM, MAX_RPM)

    temp = state["temperature_c"]
    vibr = state["vibration_mm_s"]
    if temp > WARNING_TEMPERATURE_C or vibr > WARNING_VIBRATION_MM_S:
        status = STATUS_WARNING
    else:
        status = STATUS_RUNNING

    return {
        "machine_id": MACHINE_ID,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": state["temperature_c"],
        "vibration_mm_s": state["vibration_mm_s"],
        "rpm": state["rpm"],
        "status": status,
    }


def main():
    state = {
        "temperature_c": 68.0,
        "vibration_mm_s": 0.12,
        "rpm": 1450,
    }

    publisher = TelemetryPublisher(
        host=MQTT_BROKER_HOST,
        port=MQTT_BROKER_PORT,
        topic=MQTT_TOPIC,
        availability_topic=MQTT_AVAILABILITY_TOPIC,
        client_id=MQTT_CLIENT_ID,
        qos=MQTT_QOS,
    )

    try:
        publisher.connect()
        print(
            f"Connected to MQTT broker at "
            f"{MQTT_BROKER_HOST}:{MQTT_BROKER_PORT}"
        )
        while True:
            telemetry = generate_telemetry(state)
            publisher.publish(telemetry)
            print(json.dumps(telemetry, indent=2))
            time.sleep(READ_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("Simulator stopped.")
    except (OSError, TimeoutError, RuntimeError) as error:
        print(f"Simulator error: {error}")
        raise SystemExit(1) from error
    finally:
        publisher.disconnect()


if __name__ == "__main__":
    main()
