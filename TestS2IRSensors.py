#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rcr.robots.scribbler2.Scribbler2 import Scribbler2

def main():
    robot = Scribbler2(  "/dev/rfcomm2", 500 )
    s2IRSensors = robot.getS2IRSensors()

    for i in range( 10 ):
        print( "getIRLeft: " + str( s2IRSensors.getIRLeft() ) )
        print( "getIRRight: " + str( s2IRSensors.getIRRight() ) )
        print( "getAllIR: " + str( s2IRSensors.getAllIR() ) )
        print( "getIrEx(0): " + str( s2IRSensors.getIrEx( 0, 128 ) ) )
        print( "getIrEx(1): " + str( s2IRSensors.getIrEx( 1, 128 ) ) )
    robot.close()

###
main()
