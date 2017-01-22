#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los motores del S2."""

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    """Realiza las pruebas de los motores del S2.

    Las pruebas consideran:
        robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
        s2Motors = robot.getS2Motors()

        s2Motors.getMotorStats()
        s2Motors.getEncoders()
        s2Motors.getStall()
        s2Motors.setMotors()
        s2Motors.setMotorsOff()

    """
    robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
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


if( __name__ == "__main__" ):
    main()
