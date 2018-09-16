#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de sonidos del S2."""

from __future__ import print_function

#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
#from rcr.robots.fluke2.Fluke2 import Fluke2
from rcr.robots.net2.Net2 import Net2

def main():
    """Realiza pruebas de sonido soportados por el S2.

    Las pruebas consideran:
        #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
        #robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        #robot = Net2( "192.168.145.1", 1500, 500 )
        s2Speaker = robot.getS2Speaker()

        s2Speaker.setQuiet()
        s2Speaker.setLoud()
        s2Speaker.setVolume()
        s2Speaker.setSpeaker()
        s2Speaker.setSpeaker()

    """
    #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
    #robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    robot = Net2( "192.168.145.1", 1500, 500 )
    s2Speaker = robot.getS2Speaker()

    print( "setQuiet: " + str( s2Speaker.setQuiet() ) )
    print( "setLoud: " + str( s2Speaker.setLoud() ) )
    print( "setVolume: " + str( s2Speaker.setVolume( 50 ) ) )
    print( "setSpeaker: " + str( s2Speaker.setSpeaker( 2000, 440, 880 ) ) )
    print( "setSpeaker: " + str( s2Speaker.setSpeaker( 2000, 650, 0 ) ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
