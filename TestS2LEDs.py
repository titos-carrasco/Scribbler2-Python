#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    robot = Scribbler2( "/dev/rfcomm2", 500 )
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

###
main()
