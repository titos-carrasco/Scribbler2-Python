#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    robot = Scribbler2( "/dev/rfcomm2", 500 )
    s2LightSensors = robot.getS2LightSensors()

    for i in range( 10 ):
        print( "getLeftLight: " + str( s2LightSensors.getLeftLight() ) )
        print( "getCenterLight: " + str( s2LightSensors.getCenterLight() ) )
        print( "getRightLed: " + str( s2LightSensors.getRightLed() ) )
        print( "getAllLights: " + str( s2LightSensors.getAllLights() ) )
    robot.close()

###
main()
