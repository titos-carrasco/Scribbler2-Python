#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de las operaciones en plano cartesiano del S2.

El S2 acumula los comandos de desplazamiento bajo criterio propio
y envia as respuestas cuando ese grupo ha finalizado
"""

import time

#from scribbler2.S2Serial import S2Serial
from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas de movimiento en plano cartesiano del S2.

    Los comandos de movimiento no deben tardar mas de 3000ms o se generara
    error
    """

    #robot = S2Serial( port="/dev/ttyUSB0")
    robot = S2Fluke2( port="/dev/rfcomm2")

    print( "beginPath         : ", robot.beginPath( 15 ) )

    print( "setPosn -100, -100: ", robot.setPosn( -100, -100 ) )
    print( "getPosn           : ", robot.getPosn() )
    print( "setAngle -90      : ", robot.setAngle( -90 ) )
    print( "getAngle          : ", robot.getAngle() )
    print( "setAngle 90       : ", robot.setAngle( 90 ) )
    print( "getAngle          : ", robot.getAngle() )
    print( "setPosn 0, 0      : ", robot.setPosn( 0, 0 ) )
    print( "getPosn           : ", robot.getPosn() )

    print( "moveTo 0, 100     : ", robot.moveTo( 0, 100 ) )
    print( "getAngle          : ", robot.getAngle() )
    print( "moveTo 0, -100    : ", robot.moveTo( 0, -100) )
    print( "getAngle          : ", robot.getAngle() )
    print( "moveTo 0, 100     : ", robot.moveTo( 0, 100 ) )
    print( "getAngle          : ", robot.getAngle() )

    print( "moveTo 0, 200     : ", robot.moveTo( 0, 200 ) )
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
    print( "arcBy 100, 100, 45: ", robot.arcBy( 100, 100, 45 ) )
    print( "getPosn           : ", robot.getPosn() )
    print( "getAngle          : ", robot.getAngle() )

    print( "endPath           : ", robot.endPath() )

    robot.close()


if( __name__ == "__main__" ):
    main()
