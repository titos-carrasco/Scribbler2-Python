#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los elementos internos del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los elementos internos del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )

    print( "getInfo      : ", robot.getInfo() )
    print( "getAllSensors: ", robot.getAllSensors() )
    print( "setPass      : ", robot.setPass( "1234567898765432" ) )
    print( "getPass      : ", robot.getPass() )
    print( "setPass      : ", robot.setPass( "ABCDEFGHIHGFRDCB" ) )
    print( "getPass      : ", robot.getPass() )
    print( "setName      : ", robot.setName( "NAME1234" ) )
    print( "getName      : ", robot.getName() )
    print( "setName      : ", robot.setName( "TitosBot" ) )
    print( "getName      : ", robot.getName() )
    print( "getState     : ", robot.getState() )
    print( "setData      : ", robot.setData( bytearray( [ 8, 7, 6, 5, 4, 3, 2, 1 ] ) ) )
    print( "getData      : ", bytearray.hex( robot.getData() ) )
    print( "setSingleData: ", robot.setSingleData( 4, 44 ) )
    print( "getData      : ", bytearray.hex( robot.getData() ) )
    print( "setData      : ", robot.setData( bytearray( [ 1, 2, 3, 4, 5, 6, 7, 8 ] ) ) )
    print( "getData      : ", bytearray.hex( robot.getData() ) )

    robot.close()


if( __name__ == "__main__" ):
    main()
