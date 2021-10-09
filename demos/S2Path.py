#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de las operaciones en plano cartesiano del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de movimiento en plano cartesiano del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=20000, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=20000 )

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
