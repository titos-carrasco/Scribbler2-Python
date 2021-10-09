#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los motores del S2."""

import time

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los motores del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )

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
