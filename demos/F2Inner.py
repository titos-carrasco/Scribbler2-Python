#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los elementos internos de la tarjeta F2."""

from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los elementos internos de la tarjeta F2."""

    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )

    print( "getVersion    : ", robot.getVersion() )
    print( "identifyRobot : ", robot.identifyRobot() )
    print( "getBattery    : ", robot.getBattery() )
    print( "setForwardness: " )
    robot.setForwardness( robot.SCRIBBLER_FORWARD )
    print( "setForwardness: " )
    robot.setForwardness( robot.FLUKE_FORWARD )
    print( "setForwardness: " )
    robot.setForwardness( robot.SCRIBBLER_FORWARD )
    print( "getErrors     : " )
    print( robot.getErrors() )
    robot.resetScribbler()

    robot.close()


if( __name__ == "__main__" ):
    main()
