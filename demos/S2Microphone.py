#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test del microfono del S2."""

from __future__ import print_function

#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.robots.fluke2.Fluke2 import Fluke2
#from rcr.robots.net2.Net2 import Net2

def main():
    """Realiza las pruebas del microfono del S2.

    Las pruebas consideran:
        #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
        #robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        #robot = Net2( "192.168.145.1", 1500, 500 )
        s2Microphone = robot.getS2Microphone()

        s2Microphone.getMicEnv()
    """
    #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    #robot = Net2( "192.168.145.1", 1500, 500 )
    s2Microphone = robot.getS2Microphone()

    for i in range( 50 ):
        print( "getMicEnv: " + str( s2Microphone.getMicEnv() ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
