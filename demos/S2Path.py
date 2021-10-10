#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de las operaciones en plano cartesiano del S2."""

import time

#from scribbler2.S2Serial import S2Serial
from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas de movimiento en plano cartesiano del S2."""

    #robot = S2Serial( port="/dev/ttyUSB0", timeout=20000 )
    robot = S2Fluke2( "/dev/rfcomm2" )

    print( "beginPath         : ", robot.beginPath( 15 ) )

    print( "setPosn -100, -200: ", robot.setPosn( -100, -200 ) )
    print( "getPosn           : ", robot.getPosn() )
    print( "setPosn 0, 0      : ", robot.setPosn( 0, 0 ) )
    print( "getPosn           : ", robot.getPosn() )
    print( "setAngle -90      : ", robot.setAngle( -90 ) )
    print( "getAngle          : ", robot.getAngle() )
    print( "setAngle 90       : ", robot.setAngle( 90 ) )
    print( "getAngle          : ", robot.getAngle() )

    print( "moveTo 0, 100     : ", robot.moveTo( 0, 100 ) )
    print( "moveTo 0, -1000   : ", robot.moveTo( 0, -1000) )
    print( "moveTo 0, 1000    : ", robot.moveTo( 0, 1000 ) )

    print( "moveTo 0, 2000    : ", robot.moveTo( 0, 2000 ) )
    print( "getPosn           : ", robot.getPosn() )
    print( "getAngle          : ", robot.getAngle() )
    print( "moveBy 0, 50      : ", robot.moveBy( 0, 50 ) )
    print( "getPosn           : ", robot.getPosn() )
    print( "getAngle          : ", robot.getAngle() )
    print( "turnTo 45         : ", robot.turnTo( 45 ) )
    print( "getPosn           : ", robot.getPosn() )
    print( "getAngle          : ", robot.getAngle() )
    print( "turnBy 45         : ", robot.turnBy( 45 ) )
    print( "getPosn           : ", robot.getPosn() )
    print( "getAngle          : ", robot.getAngle() )
    print( "arcTo 100, 100, 45: ", robot.arcTo( 100, 100, 45 ) )
    print( "getPosn           : ", robot.getPosn() )
    print( "getAngle          : ", robot.getAngle() )
    print( "arcBy 100         : ", robot.arcBy( 100, 100, 45 ) )
    print( "getPosn           : ", robot.getPosn() )
    print( "getAngle          : ", robot.getAngle() )

    print( "endPath           : ", robot.endPath() )

    robot.close()


if( __name__ == "__main__" ):
    main()
