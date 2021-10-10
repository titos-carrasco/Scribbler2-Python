#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los elementos internos de la tarjeta F2."""

import time

from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas de los elementos internos de la tarjeta F2."""

    robot = S2Fluke2( "/dev/rfcomm2" )

    print( "getVersion    :", robot.getVersion() )
    print( "identifyRobot :", robot.identifyRobot() )
    print( "getBattery    :", robot.getBattery() )
    print( "setForwardness: SCRIBBLER_FORWARD" )
    robot.setForwardness( robot.SCRIBBLER_FORWARD )
    print( "setForwardness: FLUKE_FORWARD" )
    robot.setForwardness( robot.FLUKE_FORWARD )
    print( "setForwardness: SCRIBBLER_FORWARD" )
    robot.setForwardness( robot.SCRIBBLER_FORWARD )
    print( "getErrors     : " )
    print( robot.getErrors() )
    robot.resetScribbler()

    robot.close()


if( __name__ == "__main__" ):
    main()
