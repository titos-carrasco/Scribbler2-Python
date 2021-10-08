#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los LEDs de la tarjeta F2."""

import time

from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los LEDs de la tarjeta F2."""

    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )
    f2LEDs = robot.getF2LEDs()

    print( "setBrightLed: 255 " )
    f2LEDs.setBrightLed( 255 )
    time.sleep( 2.0 )
    print( "setBrightLed: 128" )
    f2LEDs.setBrightLed( 128 )
    time.sleep( 2.0 )
    print( "setBrightLed: 0" )
    f2LEDs.setBrightLed( 0 )

    robot.close()


if( __name__ == "__main__" ):
    main()
