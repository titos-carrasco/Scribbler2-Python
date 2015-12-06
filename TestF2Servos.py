#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    robot = Scribbler2( "/dev/rfcomm2", 500 )
    f2Servos = robot.getF2Servos()

    id = 0;
    for value in range(0, 256, 5):
        print("setServo(%d, %d)" % (id, value))
        f2Servos.setServo(id, value)
        Utils.pause(60)
    robot.close()

###
main()
