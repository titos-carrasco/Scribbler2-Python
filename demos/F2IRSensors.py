#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores infrarojos de la tarjeta F2."""

from __future__ import print_function

from rcr.robots.fluke2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los sensores infrarojos de la tarjeta F2.

    Las pruebas consideran:
        robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        f2IRSensors = robot.getF2IRSensors()

        f2IRSensors.setIRPower()
        f2IRSensors.getIR()

    """
    robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    f2IRSensors = robot.getF2IRSensors()

    print( "setIRPower: " )
    f2IRSensors.setIRPower( 255 )

    for i in range( 200 ):
        print( "getIR: " + str( f2IRSensors.getIR() ) )

    robot.close()


if( __name__ == "__main__" ):
    main()
