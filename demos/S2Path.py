#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de las operaciones en plano cartesiano del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de movimiento en plano cartesiano del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=20000, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=20000 )
    s2Path = robot.getS2Path()

    print( "beginPath: "         , s2Path.beginPath( 15 ) )
    print( "setPosn -100, -200: ", s2Path.setPosn( -100, -200 ) )
    print( "getPosn: "           , s2Path.getPosn() )
    print( "setPosn 0, 0: "      , s2Path.setPosn( 0, 0 ) )
    print( "getPosn: "           , s2Path.getPosn() )
    print( "setAngle -90: "      , s2Path.setAngle( -90 ) )
    print( "getAngle: "          , s2Path.getAngle() )
    print( "setAngle 90: "       , s2Path.setAngle( 90 ) )
    print( "getAngle: "          , s2Path.getAngle() )

    print( "moveTo 0, 100: "  , s2Path.moveTo( 0, 100 ) )
    print( "moveTo 0, -1000: ", s2Path.moveTo( 0, -1000) )
    print( "moveTo 0, 1000: " , s2Path.moveTo( 0, 1000 ) )

    print( "moveTo 0, 2000: "    , s2Path.moveTo( 0, 2000 ) )
    print( "getPosn: "           , s2Path.getPosn() )
    print( "getAngle: "          , s2Path.getAngle() )
    print( "moveBy 0, 50: "      , s2Path.moveBy( 0, 50 ) )
    print( "getPosn: "           , s2Path.getPosn() )
    print( "getAngle: "          , s2Path.getAngle() )
    print( "turnTo 45: "         , s2Path.turnTo( 45 ) )
    print( "getPosn: "           , s2Path.getPosn() )
    print( "getAngle: "          , s2Path.getAngle() )
    print( "turnBy 45: "         , s2Path.turnBy( 45 ) )
    print( "getPosn: "           , s2Path.getPosn() )
    print( "getAngle: "          , s2Path.getAngle() )
    print( "arcTo 100, 100, 45: ", s2Path.arcTo( 100, 100, 45 ) )
    print( "getPosn: "           , s2Path.getPosn() )
    print( "getAngle: "          , s2Path.getAngle() )
    print( "arcBy 100 : "        , s2Path.arcBy( 100, 100, 45 ) )
    print( "getPosn: "           , s2Path.getPosn() )
    print( "getAngle: "          , s2Path.getAngle() )

    print( "endPath: ", s2Path.endPath() )

    robot.close()


if( __name__ == "__main__" ):
    main()
