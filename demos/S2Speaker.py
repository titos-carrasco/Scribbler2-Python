from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        print("setQuiet  : ", self.robot.setQuiet())
        print("setLoud   : ", self.robot.setLoud())
        print("setVolume : ", self.robot.setVolume(50))
        print("setSpeaker: ", self.robot.setSpeaker(125, 440))
        print("setSpeaker: ", self.robot.setSpeaker(125, 440))
        print("setSpeaker: ", self.robot.setSpeaker(125, 370))
        print("setSpeaker: ", self.robot.setSpeaker(125, 330))
        print("setSpeaker: ", self.robot.setSpeaker(125, 440))
        print("setSpeaker: ", self.robot.setSpeaker(125, 0))
        print("setSpeaker: ", self.robot.setSpeaker(500, 523))
        print("setSpeaker: ", self.robot.setSpeaker(125, 440))
        print("setSpeaker: ", self.robot.setSpeaker(125, 440))
        print("setSpeaker: ", self.robot.setSpeaker(125, 370))
        print("setSpeaker: ", self.robot.setSpeaker(125, 330))
        print("setSpeaker: ", self.robot.setSpeaker(125, 440))
        print("setSpeaker: ", self.robot.setSpeaker(125, 0))
        print("setSpeaker: ", self.robot.setSpeaker(500, 370))
        print("setSpeaker: ", self.robot.setSpeaker(125, 440))
        print("setSpeaker: ", self.robot.setSpeaker(125, 440))
        print("setSpeaker: ", self.robot.setSpeaker(125, 370))
        print("setSpeaker: ", self.robot.setSpeaker(125, 330))
        print("setSpeaker: ", self.robot.setSpeaker(125, 440))
        print("setSpeaker: ", self.robot.setSpeaker(125, 523))
        print("setSpeaker: ", self.robot.setSpeaker(125, 587))
        print("setSpeaker: ", self.robot.setSpeaker(125, 622))
        print("setSpeaker: ", self.robot.setSpeaker(125, 659))
        print("setSpeaker: ", self.robot.setSpeaker(63, 622))
        print("setSpeaker: ", self.robot.setSpeaker(63, 659))
        print("setSpeaker: ", self.robot.setSpeaker(63, 622))
        print("setSpeaker: ", self.robot.setSpeaker(63, 659))
        print("setSpeaker: ", self.robot.setSpeaker(63, 622))
        print("setSpeaker: ", self.robot.setSpeaker(500, 659))

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
