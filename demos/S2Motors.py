import time

# from scribbler2.S2 import Robot  # conexion via cable serial
from scribbler2.Fluke2 import Robot  # conexion via bluethoot a la Fluke2


class App:
    def __init__(self, dev):
        self.robot = Robot(dev)

    def run(self):
        print("getMotorStats       : ", self.robot.getMotorStats())
        print("getEncoders         : ", self.robot.getEncoders(1))
        print("getStall            : ", self.robot.getStall())
        print("setMotors 100, -100 : ", self.robot.setMotors(100, -100))
        time.sleep(3.0)
        print("setMotors -100, 100 : ", self.robot.setMotors(-100, 100))
        time.sleep(3.0)
        print("setMotorsOff        : ", self.robot.setMotorsOff())

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
