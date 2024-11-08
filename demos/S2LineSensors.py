import time
from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        for i in range(10):
            print("getLineEx 0 : ", self.robot.getLineEx(0, 128))
            print("getLineEx 1 : ", self.robot.getLineEx(1, 128))
            print("getAllLines : ", self.robot.getAllLines())
            print("getLeftLine : ", self.robot.getLeftLine())
            print("getRightLine: ", self.robot.getRightLine())
            time.sleep(0.200)

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
