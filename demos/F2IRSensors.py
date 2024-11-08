import time
from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        print("setIRPower 255 ")
        self.robot.setIRPower(255)

        for i in range(20):
            print("getIR: ", self.robot.getIR())
            time.sleep(0.200)

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
