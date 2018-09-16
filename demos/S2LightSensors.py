#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores de luz del S2."""

from __future__ import print_function

#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
#from rcr.robots.fluke2.Fluke2 import Fluke2
from rcr.robots.net2.Net2 import Net2
from rcr.utils import Utils

def main():
    """Realiza las pruebas de los sensores de luz del S2.

    Las pruebas consideran:
        #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
        #robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        #robot = Net2( "192.168.145.1", 1500, 500 )
        s2LightSensors = robot.getS2LightSensors()

        s2LightSensors.getLeftLight()
        s2LightSensors.getCenterLight()
        s2LightSensors.getRightLed()
        s2LightSensors.getAllLights()

    """
    #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
    #robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    robot = Net2( "192.168.145.1", 1500, 500 )
    s2LightSensors = robot.getS2LightSensors()

    for i in range( 10 ):
        print( "getLeftLight: " + str( s2LightSensors.getLeftLight() ) )
        print( "getCenterLight: " + str( s2LightSensors.getCenterLight() ) )
        print( "getRightLight: " + str( s2LightSensors.getRightLight() ) )
        print( "getAllLights: " + str( s2LightSensors.getAllLights() ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
