#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores de linea del S2."""

import time

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los sensores de linea del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )

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
