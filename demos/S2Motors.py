#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los motores del S2."""

import time

#from scribbler2.S2Serial import S2Serial
from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas de los motores del S2."""

    #robot = S2Serial( "/dev/ttyUSB0" )
    robot = S2Fluke2( "/dev/rfcomm2" )

    print( "getMotorStats       : ", robot.getMotorStats() )
    print( "getEncoders         : ", robot.getEncoders( 1 ) )
    print( "getStall            : ", robot.getStall() )
    print( "setMotors 100, -100 : ", robot.setMotors( 100, -100) )
    time.sleep( 3.0 )
    print( "setMotors -100, 100 : ", robot.setMotors( -100, 100) )
    time.sleep( 3.0 )
    print( "setMotorsOff        : ", robot.setMotorsOff() )

    robot.close()


if( __name__ == "__main__" ):
    main()
