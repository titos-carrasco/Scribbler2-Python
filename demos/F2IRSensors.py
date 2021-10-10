#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores infrarojos de la tarjeta F2."""

import time

from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas de los sensores infrarojos de la tarjeta F2."""

    robot = S2Fluke2( "/dev/rfcomm2" )

    print( "setIRPower 255 " )
    robot.setIRPower( 255 )

    for i in range( 20 ):
        print( "getIR: ", robot.getIR() )
        time.sleep( 0.200 )

    robot.close()


if( __name__ == "__main__" ):
    main()
