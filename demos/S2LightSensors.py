#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los sensores de luz del S2."""

#from s2.Scribbler2 import Scribbler2
from s2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de los sensores de luz del S2."""

    #robot = Scribbler2( port="/dev/ttyUSB0", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", timeout=500 )
    s2LightSensors = robot.getS2LightSensors()

    for i in range( 10 ):
        print( "getLeftLight: "  , s2LightSensors.getLeftLight() )
        print( "getCenterLight: ", s2LightSensors.getCenterLight() )
        print( "getRightLight: " , s2LightSensors.getRightLight() )
        print( "getAllLights: "  , s2LightSensors.getAllLights() )
    robot.close()


if( __name__ == "__main__" ):
    main()
