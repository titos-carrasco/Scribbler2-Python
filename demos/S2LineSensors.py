#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores de linea del S2."""

from __future__ import print_function

#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.robots.fluke2.Fluke2 import Fluke2
#from rcr.robots.net2.Net2 import Net2

def main():
    """Realiza las pruebas de los sensores de linea del S2.

    Las pruebas consideran:
        #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
        #robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        #robot = Net2( "192.168.145.1", 1500, 500 )
        s2LineSensors = robot.getS2LineSensors()

        s2LineSensors.getLineEx()
        s2LineSensors.getAllLines()
        s2LineSensors.getLeftLine()
        s2LineSensors.getRightLine()

    """
    #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    #robot = Net2( "192.168.145.1", 1500, 500 )
    s2LineSensors = robot.getS2LineSensors()

    for i in range( 10 ):
        print( "getLineEx 0: " + str( s2LineSensors.getLineEx( 0, 128 ) ) )
        print( "getLineEx 1: " + str( s2LineSensors.getLineEx( 1, 128 ) ) )
        print( "getAllLines: " + str( s2LineSensors.getAllLines() ) )
        print( "getLeftLine: " + str( s2LineSensors.getLeftLine() ) )
        print( "getRightLine: " + str( s2LineSensors.getRightLine() ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
