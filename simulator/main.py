from datetime import datetime, timezone
import json
import random


def generate_telemetry():
    return {
        "machine_id": "motor-01",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": round(random.uniform(65.0, 75.0), 2),
        "vibration_mm_s": round(random.uniform(0.08, 0.20), 2),
        "rpm": random.randint(1430, 1470),
        "status": "running",
    }


telemetry = generate_telemetry()
print(json.dumps(telemetry, indent=2))
