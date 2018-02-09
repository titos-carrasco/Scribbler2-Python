#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores infrarojos del S2."""

from rcr.robots.scribbler2.Scribbler2 import Scribbler2

def main():
    """Realiza las pruebas de los sensores infrarojos del S2.

    Las pruebas consideran:
        robot = Scribbler2(  "/dev/rfcomm2", 9600, 500 )
        s2IRSensors = robot.getS2IRSensors()

        s2IRSensors.getIRLeft()
        s2IRSensors.getIRRight()
        s2IRSensors.getAllIR()
        s2IRSensors.getIrEx()

    """
    robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
    s2IRSensors = robot.getS2IRSensors()

    for i in range( 10 ):
        print( "getIRLeft: " + str( s2IRSensors.getIRLeft() ) )
        print( "getIRRight: " + str( s2IRSensors.getIRRight() ) )
        print( "getAllIR: " + str( s2IRSensors.getAllIR() ) )
        print( "getIrEx(0): " + str( s2IRSensors.getIrEx( 0, 128 ) ) )
        print( "getIrEx(1): " + str( s2IRSensors.getIrEx( 1, 128 ) ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
