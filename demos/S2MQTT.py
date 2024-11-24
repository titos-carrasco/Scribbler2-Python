import time
import queue
import paho.mqtt.client as mqtt  # pip install paho-mqtt

# from scribbler2.S2 import Robot  # conexion via cable serial
from scribbler2.Fluke2 import Robot  # conexion via bluethoot a la Fluke2


class App:
    def __init__(self, dev, mqtt_server, mqtt_port, mqtt_topic):
        self.robot = Robot(dev)

        self.messages = queue.Queue(1)
        self.mqtt_server = mqtt_server
        self.mqtt_port = mqtt_port
        self.mqtt_topic = mqtt_topic
        self.mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqtt_client.on_connect = self.mqttOnConnect
        self.mqtt_client.on_message = self.mqttOnMessage

    def mqttOnConnect(self, client, _userdata, _flags, _reason_code, _properties):
        """Invocada al conectar a servidor MQTT."""
        client.subscribe(self.mqtt_topic)
        print(f"Esperando en {self.mqtt_server}:{self.mqtt_port}/{self.mqtt_topic}")

    def mqttOnMessage(self, _client, _userdata, msg):
        """Invocada al recibir mensaje MQTT en algun topico suscrito."""
        try:
            self.messages.get_nowait()
        except Exception as _:  # pylint: disable=broad-except
            pass
        self.messages.put_nowait(msg)

    def run(self):
        """Realiza pruebas del S2 recibiendo comandos via MQTT."""
        self.mqtt_client.connect(self.mqtt_server, self.mqtt_port)
        self.mqtt_client.loop_start()
        time.sleep(2)

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
