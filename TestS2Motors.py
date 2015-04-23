#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    robot = Scribbler2( "/dev/rfcomm2", 500 )
    s2Motors = robot.getS2Motors()

    print( "getMotorStats: " + str( s2Motors.getMotorStats() ) )
    print( "getEncoders: " + str( s2Motors.getEncoders( 1 ) ) )
    print( "getStall: " + str( s2Motors.getStall() ) )
    print( "setMotors 100, -100 : " + str( s2Motors.setMotors( 100, -100) ) )
    Utils.pause( 3000 )
    print( "setMotors -100, 100 : " + str( s2Motors.setMotors( -100, 100) ) )
    Utils.pause( 3000 )
    print( "setMotorsOff: " + str( s2Motors.setMotorsOff() ) )
    robot.close()

###
main()
