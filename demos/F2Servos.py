import time
from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        servo_id = 0
        for value in range(0, 256, 5):
            print(f"setServo({servo_id}, {value})")
            self.robot.setServo(servo_id, value)
            time.sleep(0.06)

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
