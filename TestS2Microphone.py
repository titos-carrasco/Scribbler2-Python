#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test del microfono del S2."""

from rcr.robots.scribbler2.Scribbler2 import Scribbler2

def main():
    """Realiza las pruebas del microfono del S2.

    Las pruebas consideran:
        robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
        s2Microphone = robot.getS2Microphone()

        s2Microphone.getMicEnv()
    """
    robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
    s2Microphone = robot.getS2Microphone()

    for i in range( 50 ):
        print( "getMicEnv: " + str( s2Microphone.getMicEnv() ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
