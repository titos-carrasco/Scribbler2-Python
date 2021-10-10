#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de sonidos del S2."""

import time

#from scribbler2.S2Serial import S2Serial
from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas de sonido del S2."""

    #robot = S2Serial( "/dev/ttyUSB0" )
    robot = S2Fluke2( "/dev/rfcomm2" )

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
