#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los elementos internos del S2."""

import time

#from scribbler2.S2Serial import S2Serial
from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas de los elementos internos del S2."""

    #robot = S2Serial( "/dev/ttyUSB0" )
    robot = S2Fluke2( "/dev/rfcomm2" )

    print( "getInfo      : ", robot.getInfo() )
    print( "getAllSensors: ", robot.getAllSensors() )
    print( "setPass      : ", robot.setPass( "1234567898765432" ) )
    print( "getPass      : ", robot.getPass() )
    print( "setPass      : ", robot.setPass( "ABCDEFGHIJKLMNOP" ) )
    print( "getPass      : ", robot.getPass() )
    print( "setName      : ", robot.setName( "NAME1234" ) )
    print( "getName      : ", robot.getName() )
    print( "setName      : ", robot.setName( "TitosBot" ) )
    print( "getName      : ", robot.getName() )
    print( "getState     : ", robot.getState() )
    print( "setData      : ", robot.setData( bytes( [ 8, 7, 6, 5, 4, 3, 2, 1 ] ) ) )
    print( "getData      : ", bytes.hex( robot.getData() ) )
    print( "setSingleData: ", robot.setSingleData( 4, 255 ) )
    print( "getData      : ", bytes.hex( robot.getData() ) )
    print( "setData      : ", robot.setData( bytes( [ 1, 2, 3, 4, 5, 6, 7, 8 ] ) ) )
    print( "getData      : ", bytes.hex( robot.getData() ) )

    robot.close()


if( __name__ == "__main__" ):
    main()
