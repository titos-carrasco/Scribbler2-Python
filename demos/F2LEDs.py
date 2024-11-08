import time
from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        print("setBrightLed: 255 ")
        self.robot.setBrightLed(255)
        time.sleep(2.0)
        print("setBrightLed: 128")
        self.robot.setBrightLed(128)
        time.sleep(2.0)
        print("setBrightLed: 0")
        self.robot.setBrightLed(0)

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
