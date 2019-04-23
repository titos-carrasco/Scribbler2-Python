#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los motores del S2."""

from __future__ import print_function

#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.robots.fluke2.Fluke2 import Fluke2
#from rcr.robots.net2.Net2 import Net2
from rcr.utils import Utils

def main():
    """Realiza las pruebas de los motores del S2.

    Las pruebas consideran:
        #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
        #robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        #robot = Net2( "192.168.145.1", 1500, 500 )
        s2Motors = robot.getS2Motors()

        s2Motors.getMotorStats()
        s2Motors.getEncoders()
        s2Motors.getStall()
        s2Motors.setMotors()
        s2Motors.setMotorsOff()

    """
    #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    #robot = Net2( "192.168.145.1", 1500, 500 )
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
