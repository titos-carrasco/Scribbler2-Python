#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores infrarojos de la tarjeta F2."""

from rcr.robots.scribbler2.Scribbler2 import Scribbler2

def main():
    """Realiza las pruebas de los sensores infrarojos de la tarjeta F2.

    Las pruebas consideran:
    robot = Scribbler2( "/dev/rfcomm2", 500 )
    f2IRSensors = robot.getF2IRSensors()

    f2IRSensors.setIRPower()
    f2IRSensors.getIR()

    """
    robot = Scribbler2( "/dev/rfcomm2", 500 )
    f2IRSensors = robot.getF2IRSensors()

    print( "setIRPower: " )
    f2IRSensors.setIRPower( 255 )

    for i in range( 20 ):
        print( "getIR: " + str( f2IRSensors.getIR() ) )

    robot.close()


if( __name__ == "__main__" ):
    main()
