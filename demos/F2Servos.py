import time
from scribbler2.Fluke2 import Robot  # conexion via bluethoot a la Fluke2


class App:
    def __init__(self, dev):
        self.robot = Robot(dev)

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
