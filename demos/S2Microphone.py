#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test del microfono del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas del microfono del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )
    s2Microphone = robot.getS2Microphone()

    for i in range( 50 ):
        print( "getMicEnv: ", s2Microphone.getMicEnv() )
    robot.close()


if( __name__ == "__main__" ):
    main()
