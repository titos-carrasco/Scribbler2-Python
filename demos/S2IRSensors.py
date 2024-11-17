import time

# from scribbler2.S2 import Robot  # conexion via cable serial
from scribbler2.Fluke2 import Robot  # conexion via bluethoot a la Fluke2


class App:
    def __init__(self, dev):
        self.robot = Robot(dev)

    def run(self):
        t = time.time() + 10
        while time.time() < t:
            print("getIRLeft : ", self.robot.getIRLeft())
            print("getIRRight: ", self.robot.getIRRight())
            print("getAllIR  : ", self.robot.getAllIR())
            print("getIrEx(0): ", self.robot.getIrEx(0, 128))
            print("getIrEx(1): ", self.robot.getIrEx(1, 128))

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
