# Simulator

## Overview

This folder contains the Python machine simulator.

The simulator currently generates industrial telemetry data for an electric motor and prints it as JSON. In a later milestone, it will publish telemetry to MQTT topics.

## Telemetry Payload

Example payload:

```json
{
  "machine_id": "motor-01",
  "timestamp": "2026-06-22T10:00:00+00:00",
  "temperature_c": 68.2,
  "vibration_mm_s": 0.14,
  "rpm": 1452,
  "status": "running"
}
```

## Status Rules

- `running`: normal operating condition
- `warning`: `temperature_c > 74.0` or `vibration_mm_s > 0.18`

## Run Locally

```powershell
python simulator/main.py
```

## Stop the Simulator

Press `Ctrl+C` to stop the simulator gracefully.