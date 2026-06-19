# Project Roadmap

## Purpose

This roadmap tracks the progress of the project by splitting it into small, incremental milestones.

## Milestones

### Milestone 0 - Architecture and Project Setup

Goal:
Define the project architecture and the responsibility of each system component.

Expected outcome:
Initial architecture documentation, project README, GitHub repository, and roadmap.

Status:
Done

### Milestone 1 - Repository Structure

Goal:
Prepare a clean and versioned project structure.

Expected outcome:
A clear folder structure for backend, frontend, simulator, documentation, and infrastructure files.

Status:
Planned

### Milestone 2 - Machine Simulator

Goal:
Understand how an industrial machine can produce telemetry data.

Expected outcome:
A basic Python simulator that generates machine readings such as temperature, vibration, current, and status.

Status:
Planned

### Milestone 3 - MQTT Broker and Telemetry Publishing

Goal:
Understand why MQTT is useful in industrial and IoT scenarios.

Expected outcome:
A Mosquitto MQTT broker and a simulator that publishes telemetry messages to MQTT topics.

Status:
Planned

### Milestone 4 - FastAPI Backend

Goal:
Build a simple API backend and understand the role of an application server.

Expected outcome:
A FastAPI application with basic endpoints, request/response handling, and data validation with Pydantic.

Status:
Planned

### Milestone 5 - PostgreSQL Persistence

Goal:
Store telemetry data persistently.

Expected outcome:
A PostgreSQL database connected to the backend through SQLAlchemy models and database sessions.

Status:
Planned

### Milestone 6 - React Dashboard

Goal:
Display machine status and telemetry data in a web interface.

Expected outcome:
A React dashboard that fetches data from the backend and displays machine status and charts.

Status:
Planned

### Milestone 7 - Local AI Assistant

Goal:
Integrate a local AI model to support diagnostics and maintenance decisions.

Expected outcome:
A local AI assistant connected through the backend, using Ollama and project-specific context.

Status:
Planned

### Milestone 8 - Testing and CI

Goal:
Automate checks on every push.

Expected outcome:
Backend tests, basic frontend checks, and GitHub Actions workflows for continuous integration.

Status:
Planned

## Notes

This project is built as a learning-oriented system. Each milestone should be completed incrementally, with theory, small exercises, code review, and verification before moving to the next step.