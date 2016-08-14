#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de sonidos del S2."""

from rcr.robots.scribbler2.Scribbler2 import Scribbler2

def main():
    """Realiza pruebas de sonido soportados por el S2.

    Las pruebas consideran:
        robot = Scribbler2( "/dev/rfcomm2", 500 )
        s2Speaker = robot.getS2Speaker()

        s2Speaker.setQuiet()
        s2Speaker.setLoud()
        s2Speaker.setVolume()
        s2Speaker.setSpeaker()
        s2Speaker.setSpeaker()

    """
    robot = Scribbler2( "/dev/rfcomm2", 500 )
    s2Speaker = robot.getS2Speaker()

    print( "setQuiet: " + str( s2Speaker.setQuiet() ) )
    print( "setLoud: " + str( s2Speaker.setLoud() ) )
    print( "setVolume: " + str( s2Speaker.setVolume( 50 ) ) )
    print( "setSpeaker: " + str( s2Speaker.setSpeaker( 2000, 440, 880 ) ) )
    print( "setSpeaker: " + str( s2Speaker.setSpeaker( 2000, 650, 0 ) ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
