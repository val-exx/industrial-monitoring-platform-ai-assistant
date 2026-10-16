# Simulator

## Overview

This folder contains the Python machine simulator.

The simulator generates industrial telemetry data for an electric motor, publishes it to an MQTT broker, and prints it as JSON.
It uses one persistent MQTT connection and publishes each reading with QoS 1.

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

## MQTT Configuration

The simulator connects to:

- broker: `localhost:1883`
- topic: `factory/line-1/motor-01/telemetry`
- availability topic: `factory/line-1/motor-01/availability`
- QoS: `1`

The availability topic uses retained messages:

- `online` is published after a successful connection
- `offline` is published during a graceful shutdown
- `offline` is also configured as the Last Will for an unexpected disconnect

A new subscriber receives the current availability state immediately. The
telemetry topic is not retained because PostgreSQL will provide historical data
in a later milestone.

## Run Locally

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r simulator/requirements.txt
```

Make sure the Mosquitto broker is running, then start the simulator:

```powershell
python simulator/main.py
```

Each generated reading is published to MQTT and printed to the terminal.

## Stop the Simulator

Press `Ctrl+C` to stop the simulator gracefully.
