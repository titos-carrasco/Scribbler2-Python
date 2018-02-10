#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores de luz del S2."""

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    """Realiza las pruebas de los sensores de luz del S2.

    Las pruebas consideran:
        robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
        s2LightSensors = robot.getS2LightSensors()

        s2LightSensors.getLeftLight()
        s2LightSensors.getCenterLight()
        s2LightSensors.getRightLed()
        s2LightSensors.getAllLights()

    """
    robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
    s2LightSensors = robot.getS2LightSensors()

    for i in range( 10 ):
        print( "getLeftLight: " + str( s2LightSensors.getLeftLight() ) )
        print( "getCenterLight: " + str( s2LightSensors.getCenterLight() ) )
        print( "getRightLight: " + str( s2LightSensors.getRightLight() ) )
        print( "getAllLights: " + str( s2LightSensors.getAllLights() ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
