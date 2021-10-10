#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Demo de control del S2 desde un controlador MIDI.

Requiere del paquete python-rtmidi (pip install python-rtmidi)
"""


import rtmidi

#from scribbler2.S2Serial import S2Serial
from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Demo de control del S2 utilizando un controlador MIDI."""
    print( "Creando puerta MIDI" )
    midiIn = rtmidi.MidiIn()
    midiIn.open_virtual_port("S2 Control Port")

    print( "Conectando con el Scribbler2" )
    #robot = S2Serial( "/dev/ttyUSB0" )
    robot = S2Fluke2( "/dev/rfcomm2" )

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
                    robot.setMotors( 100, -100)
                elif( note == 49 ):
                    robot.setMotors( -100, 100)
                elif( note == 50 ):
                    robot.setMotors( 100, 100)
                elif( note == 51 ):
                    robot.setMotors( -100, -100)
                elif( note == 52 ):
                    robot.setMotorsOff()
    midiIn.close()
    robot.close()


if( __name__ == "__main__" ):
    main()
