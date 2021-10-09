#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores infrarojos de la tarjeta F2."""

import time

from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los sensores infrarojos de la tarjeta F2."""

    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )

    print( "setIRPower 255 " )
    robot.setIRPower( 255 )

    for i in range( 20 ):
        print( "getIR: ", robot.getIR() )
        time.sleep( 0.200 )

    robot.close()


if( __name__ == "__main__" ):
    main()
