import json
import time

from paho.mqtt import client as mqtt


CONNECTION_TIMEOUT_SECONDS = 5
ONLINE_PAYLOAD = "online"
OFFLINE_PAYLOAD = "offline"


class TelemetryPublisher:
    def __init__(self, host, port, topic, availability_topic, client_id, qos):
        self.host = host
        self.port = port
        self.topic = topic
        self.availability_topic = availability_topic
        self.qos = qos
        self._network_loop_started = False
        self._client = mqtt.Client(
            callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
            client_id=client_id,
            protocol=mqtt.MQTTv311,
        )
        self._client.will_set(
            topic=self.availability_topic,
            payload=OFFLINE_PAYLOAD,
            qos=self.qos,
            retain=True,
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

        self._publish(
            topic=self.availability_topic,
            payload=ONLINE_PAYLOAD,
            retain=True,
        )

    def publish(self, telemetry):
        payload = json.dumps(telemetry, separators=(",", ":"))
        self._publish(topic=self.topic, payload=payload, retain=False)

    def _publish(self, topic, payload, retain):
        message = self._client.publish(
            topic=topic,
            payload=payload,
            qos=self.qos,
            retain=retain,
        )
        message.wait_for_publish()

        if message.rc != mqtt.MQTT_ERR_SUCCESS:
            raise RuntimeError(
                f"Could not publish to {topic}: {mqtt.error_string(message.rc)}"
            )

    def disconnect(self):
        if not self._network_loop_started:
            return

        if self._client.is_connected():
            self._publish(
                topic=self.availability_topic,
                payload=OFFLINE_PAYLOAD,
                retain=True,
            )

        self._client.disconnect()
        self._client.loop_stop()
        self._network_loop_started = False
