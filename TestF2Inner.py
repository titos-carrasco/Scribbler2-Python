#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rcr.robots.scribbler2.Scribbler2 import Scribbler2

def main():
    robot = Scribbler2( "/dev/rfcomm2", 500 )
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

###
main()
