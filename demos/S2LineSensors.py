#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores de linea del S2."""

import time

#from scribbler2.S2Serial import S2Serial
from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas de los sensores de linea del S2."""

    #robot = S2Serial( "/dev/ttyUSB0" )
    robot = S2Fluke2( "/dev/rfcomm2" )

    for i in range( 10 ):
        print( "getLineEx 0 : ", robot.getLineEx( 0, 128 ) )
        print( "getLineEx 1 : ", robot.getLineEx( 1, 128 ) )
        print( "getAllLines : ", robot.getAllLines() )
        print( "getLeftLine : ", robot.getLeftLine() )
        print( "getRightLine: ", robot.getRightLine() )
        time.sleep( 0.200 )

    robot.close()


if( __name__ == "__main__" ):
    main()
