#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores infrarojos del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los sensores infrarojos del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )
    s2IRSensors = robot.getS2IRSensors()

    for i in range( 10 ):
        print( "getIRLeft: " , s2IRSensors.getIRLeft() )
        print( "getIRRight: ", s2IRSensors.getIRRight() )
        print( "getAllIR: "  , s2IRSensors.getAllIR() )
        print( "getIrEx(0): ", s2IRSensors.getIrEx( 0, 128 ) )
        print( "getIrEx(1): ", s2IRSensors.getIrEx( 1, 128 ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
