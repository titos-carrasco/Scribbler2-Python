#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los motores servo de la tarjeta F2."""

import time

from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los motores servos de la tarjeta F2."""

    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )

    id = 0;
    for value in range(0, 256, 5):
        print("setServo(%d, %d)" % (id, value))
        robot.setServo(id, value)
        time.sleep( 0.06 )

    robot.close()


if( __name__ == "__main__" ):
    main()
