#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los LEDs del S2."""

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    """Realiza las pruebas del los LEDs del S2.

    Las pruebas consideran:
        robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
        s2LEDs = robot.getS2LEDs()

        s2LEDs.setLeftLed()
        s2LEDs.setCenterLed()
        s2LEDs.setRightLed()
        s2LEDs.setAllLed()

    """
    robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
    s2LEDs = robot.getS2LEDs()

    print( "setLeftLed: " + str( s2LEDs.setLeftLed( True ) ) )
    Utils.pause( 2000 )
    print( "setLeftLed: " + str( s2LEDs.setLeftLed( False ) ) )
    Utils.pause( 2000 )
    print( "setCenterLed: " + str( s2LEDs.setCenterLed( True ) ) )
    Utils.pause( 2000 )
    print( "setCenterLed: " + str( s2LEDs.setCenterLed( False ) ) )
    Utils.pause( 2000 )
    print( "setRightLed: " + str( s2LEDs.setRightLed( True ) ) )
    Utils.pause( 2000 )
    print( "setRightLed: " + str( s2LEDs.setRightLed( False ) ) )
    Utils.pause( 2000 )
    print( "setAllLed: " + str( s2LEDs.setAllLed( 1, 1, 1 ) ) )
    Utils.pause( 2000 )
    print( "setAllLed: " + str( s2LEDs.setAllLed( 0, 0, 0 ) ) )
    Utils.pause( 2000 )
    robot.close()


if( __name__ == "__main__" ):
    main()
