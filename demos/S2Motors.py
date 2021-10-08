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
    s2Motors = robot.getS2Motors()

    print( "getMotorStats: "       , s2Motors.getMotorStats() )
    print( "getEncoders: "         , s2Motors.getEncoders( 1 ) )
    print( "getStall: "            , s2Motors.getStall() )
    print( "setMotors 100, -100 : ", s2Motors.setMotors( 100, -100) )
    time.sleep( 3.0 )
    print( "setMotors -100, 100 : ", s2Motors.setMotors( -100, 100) )
    time.sleep( 3.0 )
    print( "setMotorsOff: "        , s2Motors.setMotorsOff() )
    robot.close()


if( __name__ == "__main__" ):
    main()
