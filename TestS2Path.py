#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de las operaciones en plano cartesiano del S2."""

from rcr.robots.scribbler2.Scribbler2 import Scribbler2

def main():
    """Realiza las pruebas de movimiento en plano cartesiano del S2.

    Las pruebas consideran:
        robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
        s2Path = robot.getS2Path()

        s2Path.beginPath()
        s2Path.setPosn()
        s2Path.getPosn()
        s2Path.setAngle()
        s2Path.getAngle()
        s2Path.moveTo()
        s2Path.moveBy()
        s2Path.turnTo()
        s2Path.turnBy()
        s2Path.arcTo()
        s2Path.arcBy()
        s2Path.endPath()

    """
    robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
    s2Path = robot.getS2Path()

    print( "beginPath: " + str( s2Path.beginPath( 15 ) ) )
    print( "setPosn -100, -200: " + str( s2Path.setPosn( -100, -200 ) ) )
    print( "getPosn: " + str( s2Path.getPosn() ) )
    print( "setPosn 0, 0: " + str( s2Path.setPosn( 0, 0 ) ) )
    print( "getPosn: " + str( s2Path.getPosn() ) )
    print( "setAngle -90: " + str( s2Path.setAngle( -90 ) ) )
    print( "getAngle: " + str( s2Path.getAngle() ) )
    print( "setAngle 90: " + str( s2Path.setAngle( 90 ) ) )
    print( "getAngle: " + str( s2Path.getAngle() ) )

    print( "moveTo 0, 100: " + str( s2Path.moveTo( 0, 100 ) ) )
    print( "moveTo 0, -1000: " + str( s2Path.moveTo( 0, -1000) ) )
    print( "moveTo 0, 1000: " + str( s2Path.moveTo( 0, 1000 ) ) )

    print( "moveTo 0, 2000: " + str( s2Path.moveTo( 0, 2000 ) ) )
    print( "getPosn: " + str( s2Path.getPosn() ) )
    print( "getAngle: " + str( s2Path.getAngle() ) )
    print( "moveBy 0, 50: " + str( s2Path.moveBy( 0, 50 ) ) )
    print( "getPosn: " + str( s2Path.getPosn() ) )
    print( "getAngle: " + str( s2Path.getAngle() ) )
    print( "turnTo 45: " + str( s2Path.turnTo( 45 ) ) )
    print( "getPosn: " + str( s2Path.getPosn() ) )
    print( "getAngle: " + str( s2Path.getAngle() ) )
    print( "turnBy 45: " + str( s2Path.turnBy( 45 ) ) )
    print( "getPosn: " + str( s2Path.getPosn() ) )
    print( "getAngle: " + str( s2Path.getAngle() ) )
    print( "arcTo 100, 100, 45: "+ str( s2Path.arcTo( 100, 100, 45 ) ) )
    print( "getPosn: " + str( s2Path.getPosn() ) )
    print( "getAngle: " + str( s2Path.getAngle() ) )
    print( "arcBy 100 : " + str( s2Path.arcBy( 100, 100, 45 ) ) )
    print( "getPosn: " + str( s2Path.getPosn() ) )
    print( "getAngle: " + str( s2Path.getAngle() ) )

    print( "endPath: " + str( s2Path.endPath() ) )

    robot.close()


if( __name__ == "__main__" ):
    main()
