#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los elementos internos de la tarjeta F2."""

from __future__ import print_function

from rcr.robots.fluke2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los elementos internos de la tarjeta F2.

    Las pruebas consideran:
        robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        f2Inner = robot.getF2Inner()

        f2Inner.getVersion()
        f2Inner.identifyRobot()
        f2Inner.getBattery()
        f2Inner.setForwardness()
        f2Inner.getErrors()
        f2Inner.resetScribbler()

    """
    robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    f2Inner = robot.getF2Inner()

    print( "getVersion: " + str( f2Inner.getVersion() ) )
    print( "identifyRobot: " + str( f2Inner.identifyRobot() ) )
    print( "getBattery: " + str( f2Inner.getBattery() ) )
    print( "setForwardness: " )
    f2Inner.setForwardness( f2Inner.SCRIBBLER_FORWARD )
    print( "setForwardness: " )
    f2Inner.setForwardness( f2Inner.FLUKE_FORWARD )
    print( "setForwardness: " )
    f2Inner.setForwardness( f2Inner.SCRIBBLER_FORWARD )
    print( "getErrors: " )
    print( f2Inner.getErrors() )
    f2Inner.resetScribbler()
    robot.close()


if( __name__ == "__main__" ):
    main()
