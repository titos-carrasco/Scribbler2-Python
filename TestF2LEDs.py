#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    robot = Scribbler2( "/dev/rfcomm2", 500 )
    f2LEDs = robot.getF2LEDs()

    print( "setBrightLed: " )
    f2LEDs.setBrightLed( 255 )
    Utils.pause( 2000 )
    print( "setBrightLed: " )
    f2LEDs.setBrightLed( 128 )
    Utils.pause( 2000 )
    print( "setBrightLed: " )
    f2LEDs.setBrightLed( 0 )

    robot.close()

###
main()
