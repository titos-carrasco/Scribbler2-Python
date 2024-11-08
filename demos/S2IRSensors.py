from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        for i in range(30):
            print("getIRLeft : ", self.robot.getIRLeft())
            print("getIRRight: ", self.robot.getIRRight())
            print("getAllIR  : ", self.robot.getAllIR())
            print("getIrEx(0): ", self.robot.getIrEx(0, 128))
            print("getIrEx(1): ", self.robot.getIrEx(1, 128))

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
