#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores de linea del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los sensores de linea del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )
    s2LineSensors = robot.getS2LineSensors()

    for i in range( 10 ):
        print( "getLineEx 0: " , s2LineSensors.getLineEx( 0, 128 ) )
        print( "getLineEx 1: " , s2LineSensors.getLineEx( 1, 128 ) )
        print( "getAllLines: " , s2LineSensors.getAllLines() )
        print( "getLeftLine: " , s2LineSensors.getLeftLine() )
        print( "getRightLine: ", s2LineSensors.getRightLine() )
    robot.close()


if( __name__ == "__main__" ):
    main()
