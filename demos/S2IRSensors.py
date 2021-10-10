#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores infrarojos del S2."""

import time

#from scribbler2.S2Serial import S2Serial
from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas de los sensores infrarojos del S2."""

    #robot = S2Serial( "/dev/ttyUSB0" )
    robot = S2Fluke2( "/dev/rfcomm2" )

    for i in range( 30 ):
        print( "getIRLeft : ", robot.getIRLeft() )
        print( "getIRRight: ", robot.getIRRight() )
        print( "getAllIR  : ", robot.getAllIR() )
        print( "getIrEx(0): ", robot.getIrEx( 0, 128 ) )
        print( "getIrEx(1): ", robot.getIrEx( 1, 128 ) )

    robot.close()


if( __name__ == "__main__" ):
    main()
