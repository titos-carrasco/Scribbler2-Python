#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de sonidos del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )
    s2Speaker = robot.getS2Speaker()

    print( "setQuiet: "  , s2Speaker.setQuiet() )
    print( "setLoud: "   , s2Speaker.setLoud() )
    print( "setVolume: " , s2Speaker.setVolume( 50 ) )
    print( "setSpeaker: ", s2Speaker.setSpeaker( 2000, 440, 880 ) )
    print( "setSpeaker: ", s2Speaker.setSpeaker( 2000, 650, 0 ) )
    robot.close()


if( __name__ == "__main__" ):
    main()
