# Industrial Monitoring Platform - Architecture

## Goal

The goal of this system is to collect data from industrial machines, such as temperature, vibration, and electrical current. The data is stored as historical telemetry and displayed to the operator through a graphical interface.

In case of anomalies, the system can help evaluate the situation and suggest possible diagnostic or maintenance actions.

## System Components

1. simulator -> generates simulated data from an industrial machine and publishes it to an MQTT topic
2. MQTT broker -> receives messages from publishers and distributes them to subscribers subscribed to that topic
3. backend -> validates the received data, stores it in the database, and exposes it to the frontend through APIs
4. database -> stores the historical telemetry data validated by the backend
5. frontend -> displays data received from the backend through a graphical interface, such as a dashboard
6. AI assistant -> uses telemetry data, alerts, and technical documentation to suggest possible causes and maintenance actions

## Data Flow

1. The simulator generates machine data.
2. The simulator publishes data to an MQTT topic.
3. The MQTT broker receives the message.
4. The backend, subscribed to the topic, receives the message.
5. The backend validates the data.
6. The backend stores the data in the database.
7. The frontend requests data through APIs.
8. The backend reads data from the database.
9. The frontend displays the dashboard.
10. The user requests a diagnosis from the AI assistant through the frontend.
11. The backend prepares the context and queries the local AI model.
12. The frontend displays the diagnostic response.

## Why This Architecture

The components are separated so that each one has a clear responsibility.

The simulator generates data, the MQTT broker manages message communication, the backend validates and coordinates the system, the database stores historical data, and the frontend displays information to the user.

This architecture makes the system safer because the frontend does not access the database directly. It also makes the project easier to test and modify, because each component can evolve without rewriting the entire system.

## Open Questions

- How do we distinguish anomalous data from invalid data?
- How often should the simulator send telemetry data?