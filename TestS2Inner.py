#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    robot = Scribbler2(  "/dev/rfcomm2", 500 )
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

###
main()
