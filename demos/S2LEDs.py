#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los LEDs del S2."""

import time

#from scribbler2.S2Serial import S2Serial
from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas del los LEDs del S2."""

    #robot = S2Serial( "/dev/ttyUSB0" )
    robot = S2Fluke2( "/dev/rfcomm2" )

    print( "setLeftLed  : ", robot.setLeftLed( True ) )
    time.sleep( 2.0 )
    print( "setLeftLed  : ", robot.setLeftLed( False ) )
    time.sleep( 2.0 )
    print( "setCenterLed: ", robot.setCenterLed( True ) )
    time.sleep( 2.0 )
    print( "setCenterLed: ", robot.setCenterLed( False ) )
    time.sleep( 2.0 )
    print( "setRightLed : ", robot.setRightLed( True ) )
    time.sleep( 2.0 )
    print( "setRightLed : ", robot.setRightLed( False ) )
    time.sleep( 2.0 )
    print( "setAllLed   : ", robot.setAllLed( 1, 1, 1 ) )
    time.sleep( 2.0 )
    print( "setAllLed   : ", robot.setAllLed( 0, 0, 0 ) )
    time.sleep( 2.0 )

    robot.close()


if( __name__ == "__main__" ):
    main()
