import time
from scribbler2.Fluke2 import Robot  # conexion via bluethoot a la Fluke2


class App:
    def __init__(self, dev):
        self.robot = Robot(dev)

    def run(self):
        print("setIRPower 255 ")
        self.robot.setIRPower(255)

        for _i in range(20):
            print("getIR: ", self.robot.getIR())
            time.sleep(0.200)

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
