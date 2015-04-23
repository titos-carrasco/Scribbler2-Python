#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rcr.robots.scribbler2.Scribbler2 import Scribbler2

def main():
    robot = Scribbler2( "/dev/rfcomm2", 500 )
    s2Microphone = robot.getS2Microphone()

    for i in range( 50 ):
        print( "getMicEnv: " + str( s2Microphone.getMicEnv() ) )
    robot.close()

###
main()
