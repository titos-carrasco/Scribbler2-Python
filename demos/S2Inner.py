#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los elementos internos del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los elementos internos del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )
    s2Inner = robot.getS2Inner()

    print( "getInfo: "      , s2Inner.getInfo() )
    print( "getAllSensors: ", s2Inner.getAllSensors() )
    print( "setPass: "      , s2Inner.setPass( "1234567898765432" ) )
    print( "getPass: "      , s2Inner.getPass() )
    print( "setPass: "      , s2Inner.setPass( "ABCDEFGHIHGFRDCB" ) )
    print( "getPass: "      , s2Inner.getPass() )
    print( "setName: "      , s2Inner.setName( "NAME1234" ) )
    print( "getName: "      , s2Inner.getName() )
    print( "setName: "      , s2Inner.setName( "TitosBot" ) )
    print( "getName: "      , s2Inner.getName() )
    print( "getState: "     , s2Inner.getState() )
    print( "setData: "      , s2Inner.setData( bytearray( [ 1, 2, 3, 4, 5, 6, 7, 8 ] ) ) )
    print( "getData: "      , bytearray.hex( s2Inner.getData() ) )
    print( "setData: "      , s2Inner.setData( bytearray( [ 8, 7, 6, 5, 4, 3, 2, 1 ] ) ) )
    print( "getData: "      , bytearray.hex( s2Inner.getData() ) )
    print( "setSingleData: ", s2Inner.setSingleData( 4, 44 ) )
    print( "getData: "      , bytearray.hex( s2Inner.getData() ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
