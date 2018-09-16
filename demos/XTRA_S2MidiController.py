#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Demo de control del S2 desde un controlador MIDI.

Requiere del paquete rtmidi (pip install python-rtmidi)
"""

from __future__ import print_function

import rtmidi

#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.robots.fluke2.Fluke2 import Fluke2
from rcr.utils import Utils


def main():
    """Demo de control del S2 utilizando un controlador MIDI."""
    print( "Creando puerta MIDI" )
    midiIn = rtmidi.MidiIn()
    midiIn.open_virtual_port("S2 Control Port")

    print( "Conectando con el Scribbler2" )
    #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
    robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    #robot = Net2( "192.168.145.1", 1500, 500 )
    s2Motors = robot.getS2Motors()

    print( "Conecte la puerta del Controlador Midi a la puerta virtual creada" )
    while( True ):
        cmd = None
        while( True ):
            data = midiIn.get_message()
            if( data == None ):
                continue
            msg = data[0]
            event = msg[0] & 0xF0

            # note on event
            if( event == 0x90 ):
                channel = msg[0] & 0x0F
                note = msg[1]
                velocity = msg[2]
                print( channel, note, velocity )
                if( note == 48 ):
                    s2Motors.setMotors( 100, -100)
                elif( note == 49 ):
                    s2Motors.setMotors( -100, 100)
                elif( note == 50 ):
                    s2Motors.setMotors( 100, 100)
                elif( note == 51 ):
                    s2Motors.setMotors( -100, -100)
                elif( note == 52 ):
                    s2Motors.setMotorsOff()
    midiIn.close()
    robot.close()


if( __name__ == "__main__" ):
    main()
