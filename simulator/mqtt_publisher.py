import json
import time

from paho.mqtt import client as mqtt


CONNECTION_TIMEOUT_SECONDS = 5


class TelemetryPublisher:
    def __init__(self, host, port, topic, client_id, qos):
        self.host = host
        self.port = port
        self.topic = topic
        self.qos = qos
        self._network_loop_started = False
        self._client = mqtt.Client(
            callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
            client_id=client_id,
            protocol=mqtt.MQTTv311,
        )

    def connect(self):
        self._client.connect(self.host, self.port)
        self._client.loop_start()
        self._network_loop_started = True

        deadline = time.monotonic() + CONNECTION_TIMEOUT_SECONDS
        while not self._client.is_connected():
            if time.monotonic() >= deadline:
                self.disconnect()
                raise TimeoutError(
                    f"MQTT connection to {self.host}:{self.port} timed out"
                )
            time.sleep(0.05)

    def publish(self, telemetry):
        payload = json.dumps(telemetry, separators=(",", ":"))
        message = self._client.publish(
            topic=self.topic,
            payload=payload,
            qos=self.qos,
        )
        message.wait_for_publish()

        if message.rc != mqtt.MQTT_ERR_SUCCESS:
            raise RuntimeError(
                f"Could not publish MQTT message: {mqtt.error_string(message.rc)}"
            )

    def disconnect(self):
        if not self._network_loop_started:
            return

        self._client.disconnect()
        self._client.loop_stop()
        self._network_loop_started = False
