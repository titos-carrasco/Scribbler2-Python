#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los LEDs del S2."""

import time

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas del los LEDs del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )

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
