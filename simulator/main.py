from datetime import datetime, timezone
import json
import random
import time

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


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def generate_telemetry(state):
    state["temperature_c"] = round(clamp(state["temperature_c"] + random.uniform(-TEMPERATURE_DELTA_C, TEMPERATURE_DELTA_C), MIN_TEMPERATURE_C, MAX_TEMPERATURE_C), 2)
    state["vibration_mm_s"] = round(clamp(state["vibration_mm_s"] + random.uniform(-VIBRATION_DELTA_MM_S, VIBRATION_DELTA_MM_S), MIN_VIBRATION_MM_S, MAX_VIBRATION_MM_S), 2)
    state["rpm"] = clamp(state["rpm"] + random.randint(-RPM_DELTA, RPM_DELTA), MIN_RPM, MAX_RPM)
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

    try:
        while True:
            telemetry = generate_telemetry(state)
            print(json.dumps(telemetry, indent=2))
            time.sleep(READ_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("Simulator stopped.")


if __name__ == "__main__":
    main()
