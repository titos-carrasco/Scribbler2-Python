import time
from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        for i in range(50):
            print("getMicEnv: ", self.robot.getMicEnv())
            time.sleep(0.200)

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
