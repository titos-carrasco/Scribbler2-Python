#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los motores servo de la tarjeta F2."""

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    """Realiza las pruebas de los motores servos de la tarjeta F2.

    Las pruebas consideran:
        robot = Scribbler2( "/dev/rfcomm2", 500 )
        f2Servos = robot.getF2Servos()

        f2Servos.setServo()

    """
    robot = Scribbler2( "/dev/rfcomm2", 500 )
    f2Servos = robot.getF2Servos()

    id = 0;
    for value in range(0, 256, 5):
        print("setServo(%d, %d)" % (id, value))
        f2Servos.setServo(id, value)
        Utils.pause(60)
    robot.close()


if( __name__ == "__main__" ):
    main()
