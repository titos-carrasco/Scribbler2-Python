#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test del microfono del S2."""

import time

#from scribbler2.S2Serial import S2Serial
from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas del microfono del S2."""

    #robot = S2Serial( "/dev/ttyUSB0" )
    robot = S2Fluke2( "/dev/rfcomm2" )

    for i in range( 50 ):
        print( "getMicEnv: ", robot.getMicEnv() )
        time.sleep( 0.200 )

    robot.close()


if( __name__ == "__main__" ):
    main()
