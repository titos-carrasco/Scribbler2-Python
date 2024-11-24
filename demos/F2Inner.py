from scribbler2.Fluke2 import Robot  # conexion via bluethoot a la Fluke2


class App:
    def __init__(self, dev):
        self.robot = Robot(dev)

    def run(self):
        print("getVersion    :", self.robot.getVersion())
        print("identifyRobot :", self.robot.identifyRobot())
        print("getBattery    :", self.robot.getBattery())
        print("setForwardness: SCRIBBLER_FORWARD")
        self.robot.setForwardness(self.robot.SCRIBBLER_FORWARD)
        print("setForwardness: FLUKE_FORWARD")
        self.robot.setForwardness(self.robot.FLUKE_FORWARD)
        print("setForwardness: SCRIBBLER_FORWARD")
        self.robot.setForwardness(self.robot.SCRIBBLER_FORWARD)
        print("getErrors     : ")
        print(self.robot.getErrors())
        self.robot.reset()

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
