#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rcr.robots.scribbler2.Scribbler2 import Scribbler2

def main():
    robot = Scribbler2( "/dev/rfcomm2", 500 )
    f2IRSensors = robot.getF2IRSensors()

    print( "setIRPower: " )
    f2IRSensors.setIRPower( 255 )

    for i in range( 20 ):
        print( "getIR: " + str( f2IRSensors.getIR() ) )

    robot.close()

###
main()
