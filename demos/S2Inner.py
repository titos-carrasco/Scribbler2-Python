#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los elementos internos del S2."""

from __future__ import print_function

#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
#from rcr.robots.fluke2.Fluke2 import Fluke2
from rcr.robots.net2.Net2 import Net2
from rcr.utils import Utils

def main():
    """Realiza las pruebas de los elementos internos del S2.

    Las pruebas consideran:
        #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
        #robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        #robot = Net2( host="192.168.145.1", port=1500, timeout=500 )
        s2Inner = robot.getS2Inner()

        s2Inner.getInfo()
        s2Inner.getAllSensors()
        s2Inner.setPass()
        s2Inner.getPass()
        s2Inner.setName()
        s2Inner.getName()
        s2Inner.getState()
        s2Inner.setData()
        s2Inner.setSingleData()

    """
    #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
    #robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    robot = Net2( host="192.168.145.1", port=1500, timeout=500 )
    s2Inner = robot.getS2Inner()

    print( "getInfo: " + str( s2Inner.getInfo() ) )
    print( "getAllSensors: " + str( s2Inner.getAllSensors() ) )
    print( "setPass: " + str( s2Inner.setPass( "1234567898765432" ) ) )
    print( "getPass: " + str( s2Inner.getPass() ) )
    print( "setPass: " + str( s2Inner.setPass( "ABCDEFGHIHGFRDCB" ) ) )
    print( "getPass: " + str( s2Inner.getPass() ) )
    print( "setName: " + str( s2Inner.setName( "NAME1234" ) ) )
    print( "getName: " + str( s2Inner.getName() ) )
    print( "setName: " + str( s2Inner.setName( "LilyBot" ) ) )
    print( "getName: " + str( s2Inner.getName() ) )
    print( "getState: " + str( s2Inner.getState() ) )
    print( "setData: " + str( s2Inner.setData( bytearray( [ 1, 2, 3, 4, 5, 6, 7, 8 ] ) ) ) )
    print( "getData: " + str( Utils.bytesToHex( s2Inner.getData() ) ) )
    print( "setData: " + str( s2Inner.setData( bytearray( [ 8, 7, 6, 5, 4, 3, 2, 1 ] ) ) ) )
    print( "getData: " + str( Utils.bytesToHex( s2Inner.getData() ) ) )
    print( "setSingleData: " + str( s2Inner.setSingleData( 4, 44 ) ) )
    print( "getData: " + str( Utils.bytesToHex( s2Inner.getData() ) ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
