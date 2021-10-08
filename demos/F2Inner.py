#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los elementos internos de la tarjeta F2."""

from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los elementos internos de la tarjeta F2."""

    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )
    f2Inner = robot.getF2Inner()

    print( "getVersion: "   , f2Inner.getVersion() )
    print( "identifyRobot: ", f2Inner.identifyRobot() )
    print( "getBattery: "   , f2Inner.getBattery() )
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
