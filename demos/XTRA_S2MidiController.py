#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Demo de control del S2 desde un controlador MIDI.

Requiere del paquete pyrtmidi (pip install rtmidi)
"""

import rtmidi

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils


def main():
    """Demo de control del S2 utilizando un controlador MIDI."""
    print( "Creando puerta MIDI" )
    midiIn = rtmidi.RtMidiIn()
    midiIn.openVirtualPort("S2 Control Port")

    print( "Conectando con el Scribbler2" )
    robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
    s2Motors = robot.getS2Motors()

    print( "Conecte la puerta del Controlador Midi a la puerta virtual creada" )
    while( True ):
        cmd = None
        while( True ):
            message = midiIn.getMessage()
            if( message == None ):
                continue
            if( message.isNoteOn() ):
                note = message.getNoteNumber()
                print( note )
                if( note == 48 ):
                    s2Motors.setMotors( 100, -100)
                elif( note == 52 ):
                    s2Motors.setMotors( -100, 100)
                elif( note == 55 ):
                    s2Motors.setMotors( 100, 100)
                elif( note == 59 ):
                    s2Motors.setMotors( -100, -100)
                elif( note == 83 ):
                    s2Motors.setMotorsOff()
    midiIn.close()
    robot.close()


if( __name__ == "__main__" ):
    main()
