from datetime import datetime, timezone
import json
import random
import time


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def generate_telemetry(state):
    state["temperature_c"] = round(clamp(state["temperature_c"] + random.uniform(-0.3, 0.3), 65.0, 75.0), 2)
    state["vibration_mm_s"] = round(clamp(state["vibration_mm_s"] + random.uniform(-0.02, 0.02), 0.08, 0.20), 2)
    state["rpm"] = clamp(state["rpm"] + random.randint(-5, 5), 1430, 1470)
    return {
        "machine_id": "motor-01",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": state["temperature_c"],
        "vibration_mm_s": state["vibration_mm_s"],
        "rpm": state["rpm"],
        "status": "running",
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
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulator stopped.")


if __name__ == "__main__":
    main()
