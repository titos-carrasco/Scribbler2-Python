import time

# from scribbler2.S2 import Robot  # conexion via cable serial
from scribbler2.Fluke2 import Robot  # conexion via bluethoot a la Fluke2


class App:
    def __init__(self, dev):
        self.robot = Robot(dev)

    def run(self):
        t = time.time() + 10
        while time.time() < t:
            print("getMicEnv: ", self.robot.getMicEnv())

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
