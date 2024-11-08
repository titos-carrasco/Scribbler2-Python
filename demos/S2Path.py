"""Test de las operaciones en plano cartesiano del S2.

El S2 acumula los comandos de desplazamiento bajo criterio propio
y envia las respuestas cuando ese grupo ha finalizado
"""

from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        """
        Los comandos de movimiento no deben tardar mas de 3000ms o se generara
        error
        """
        print("beginPath         : ", self.robot.beginPath(15))

        print("setPosn -100, -100: ", self.robot.setPosn(-100, -100))
        print("getPosn           : ", self.robot.getPosn())
        print("setAngle -90      : ", self.robot.setAngle(-90))
        print("getAngle          : ", self.robot.getAngle())
        print("setAngle 90       : ", self.robot.setAngle(90))
        print("getAngle          : ", self.robot.getAngle())
        print("setPosn 0, 0      : ", self.robot.setPosn(0, 0))
        print("getPosn           : ", self.robot.getPosn())

        print("moveTo 0, 100     : ", self.robot.moveTo(0, 100))
        print("getAngle          : ", self.robot.getAngle())
        print("moveTo 0, -100    : ", self.robot.moveTo(0, -100))
        print("getAngle          : ", self.robot.getAngle())
        print("moveTo 0, 100     : ", self.robot.moveTo(0, 100))
        print("getAngle          : ", self.robot.getAngle())

        print("moveTo 0, 200     : ", self.robot.moveTo(0, 200))
        print("getPosn           : ", self.robot.getPosn())
        print("getAngle          : ", self.robot.getAngle())
        print("moveBy 0, 50      : ", self.robot.moveBy(0, 50))
        print("getPosn           : ", self.robot.getPosn())
        print("getAngle          : ", self.robot.getAngle())
        print("turnTo 45         : ", self.robot.turnTo(45))
        print("getPosn           : ", self.robot.getPosn())
        print("getAngle          : ", self.robot.getAngle())
        print("turnBy 45         : ", self.robot.turnBy(45))
        print("getPosn           : ", self.robot.getPosn())
        print("getAngle          : ", self.robot.getAngle())
        print("arcTo 100, 100, 45: ", self.robot.arcTo(100, 100, 45))
        print("getPosn           : ", self.robot.getPosn())
        print("getAngle          : ", self.robot.getAngle())
        print("arcBy 100, 100, 45: ", self.robot.arcBy(100, 100, 45))
        print("getPosn           : ", self.robot.getPosn())
        print("getAngle          : ", self.robot.getAngle())

        print("endPath           : ", self.robot.endPath())

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
