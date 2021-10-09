#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de sonidos del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )

    print( "setQuiet  : ", robot.setQuiet() )
    print( "setLoud   : ", robot.setLoud() )
    print( "setVolume : ", robot.setVolume( 50 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 440 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 440 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 370 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 330 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 440 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 0 ) )
    print( "setSpeaker: ", robot.setSpeaker( 500, 523 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 440 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 440 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 370 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 330 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 440 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 0 ) )
    print( "setSpeaker: ", robot.setSpeaker( 500, 370 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 440 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 440 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 370 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 330 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 440 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 523 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 587 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 622 ) )
    print( "setSpeaker: ", robot.setSpeaker( 125, 659 ) )
    print( "setSpeaker: ", robot.setSpeaker( 63, 622 ) )
    print( "setSpeaker: ", robot.setSpeaker( 63, 659 ) )
    print( "setSpeaker: ", robot.setSpeaker( 63, 622 ) )
    print( "setSpeaker: ", robot.setSpeaker( 63, 659 ) )
    print( "setSpeaker: ", robot.setSpeaker( 63, 622 ) )
    print( "setSpeaker: ", robot.setSpeaker( 500, 659 ) )

    robot.close()


if( __name__ == "__main__" ):
    main()
