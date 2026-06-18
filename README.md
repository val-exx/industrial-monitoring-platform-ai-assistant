# Industrial Monitoring Platform with AI Assistant

## Overview

This project is a learning-oriented industrial monitoring platform. It simulates industrial machines, collects telemetry data, stores historical readings, displays machine status in a web dashboard, and uses a local AI assistant to support diagnostics and maintenance decisions.

## Project Goals

- Simulate industrial machines
- Collect telemetry through MQTT
- Store historical data in PostgreSQL
- Expose backend APIs with FastAPI
- Display machine status in a React dashboard
- Use a local AI assistant for diagnostics

## Planned Architecture

1. Simulator -> generates simulated data from an industrial machine and publishes it to an MQTT topic
2. MQTT broker -> receives messages from publishers and distributes them to subscribers of that topic
3. Backend -> validates the received data, stores it in the database, and exposes it to the frontend through APIs
4. Database -> stores the historical telemetry data validated by the backend
5. Frontend -> displays data received from the backend through a graphical interface, such as a dashboard
6. AI assistant -> uses telemetry data, alerts, and technical documentation to suggest possible causes and maintenance actions

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- Docker Compose
- MQTT
- Mosquitto
- React
- Vite
- Chart.js
- Ollama
- ChromaDB
- RAG architecture
- GitHub Actions

## Project Status

The project is in the initial architecture and setup phase.

## Documentation

- [Architecture](docs/architecture.md)