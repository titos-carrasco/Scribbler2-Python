import time

# from scribbler2.S2 import Robot  # conexion via cable serial
from scribbler2.Fluke2 import Robot  # conexion via bluethoot a la Fluke2


class App:
    def __init__(self, dev):
        self.robot = Robot(dev)

    def run(self):
        t = time.time() + 10
        while time.time() < t:
            print("getLineEx 0 : ", self.robot.getLineEx(0, 128))
            print("getLineEx 1 : ", self.robot.getLineEx(1, 128))
            print("getAllLines : ", self.robot.getAllLines())
            print("getLeftLine : ", self.robot.getLeftLine())
            print("getRightLine: ", self.robot.getRightLine())

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
