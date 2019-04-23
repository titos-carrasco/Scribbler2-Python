#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los LEDs del S2."""

from __future__ import print_function

#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.robots.fluke2.Fluke2 import Fluke2
#from rcr.robots.net2.Net2 import Net2
from rcr.utils import Utils

def main():
    """Realiza las pruebas del los LEDs del S2.

    Las pruebas consideran:
        #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
        #robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        #robot = Net2( "192.168.145.1", 1500, 500 )
        s2LEDs = robot.getS2LEDs()

        s2LEDs.setLeftLed()
        s2LEDs.setCenterLed()
        s2LEDs.setRightLed()
        s2LEDs.setAllLed()

    """
    #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    #robot = Net2( "192.168.145.1", 1500, 500 )
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
