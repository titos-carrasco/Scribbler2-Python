#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores infrarojos del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los sensores infrarojos del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )

    for i in range( 30 ):
        print( "getIRLeft : ", robot.getIRLeft() )
        print( "getIRRight: ", robot.getIRRight() )
        print( "getAllIR  : ", robot.getAllIR() )
        print( "getIrEx(0): ", robot.getIrEx( 0, 128 ) )
        print( "getIrEx(1): ", robot.getIrEx( 1, 128 ) )

    robot.close()


if( __name__ == "__main__" ):
    main()
