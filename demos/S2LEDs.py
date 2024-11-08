import time
from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        print("setLeftLed  : ", self.robot.setLeftLed(True))
        time.sleep(2.0)
        print("setLeftLed  : ", self.robot.setLeftLed(False))
        time.sleep(2.0)
        print("setCenterLed: ", self.robot.setCenterLed(True))
        time.sleep(2.0)
        print("setCenterLed: ", self.robot.setCenterLed(False))
        time.sleep(2.0)
        print("setRightLed : ", self.robot.setRightLed(True))
        time.sleep(2.0)
        print("setRightLed : ", self.robot.setRightLed(False))
        time.sleep(2.0)
        print("setAllLed   : ", self.robot.setAllLed(1, 1, 1))
        time.sleep(2.0)
        print("setAllLed   : ", self.robot.setAllLed(0, 0, 0))
        time.sleep(2.0)

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
