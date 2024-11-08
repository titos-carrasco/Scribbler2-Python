import time
import queue
import paho.mqtt.client as paho  # pip install paho-mqtt
from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev, server, port, topic):
        self.server = server
        self.port = port
        self.topic = topic

        self.robot = S2Fluke2(dev)

        self.messages = queue.Queue(1)
        self.mqtt_client = paho.Client()
        self.mqtt_client.on_connect = self._mqttOnConnect
        self.mqtt_client.on_message = self._mqttOnMessage
        self.mqtt_client.connect(server, port)
        self.mqtt_client.loop_start()

    def _mqttOnConnect(self, client, userdata, flag, rc):
        """Invocada al conectar a servidor MQTT."""

        client.subscribe(self.topic)
        print(f"Esperando en {self.server}:{self.port}/{self.topic}")

    def _mqttOnMessage(self, client, userdata, message):
        """Invocada al recibir mensaje MQTT en algun topico suscrito."""

        # si no se ha procesado el ultimo mensaje lo eliminamos
        try:
            self.messages.get_nowait()
        except queue.Empty:
            pass

        # agregamos el mensaje
        try:
            self.messages.put_nowait(message)
        except queue.Full:
            pass

    def run(self):
        """Realiza pruebas del S2 recibiendo comandos via MQTT."""
        print("Comandos:")
        print("  nombre")
        print("  izquierda")
        print("  derecha")
        print("  avanza")
        print("  retrocede")
        print("  detente")
        print("  exit")
        print("---")

        running = True
        while running:
            message = self.messages.get()
            payload = message.payload.decode("utf-8")
            print("Mensaje recibido:", payload)

            words = payload.split()
            cmd = words[0]
            if cmd == "exit":
                running = False
            elif cmd == "nombre":
                print(self.robot.getName())
            elif cmd == "izquierda":
                self.robot.setMotors(-100, 100)
            elif cmd == "derecha":
                self.robot.setMotors(100, -100)
            elif cmd == "avanza":
                self.robot.setMotors(100, 100)
            elif cmd == "retrocede":
                self.robot.setMotors(-100, -100)
            elif cmd == "detente":
                self.robot.setMotors(0, 0)
        self.mqtt_client.loop_stop()
        self.robot.close()


# ---
app = App("/dev/rfcomm2", "test.mosquitto.org", 1883, "rcr/s2")
app.run()
