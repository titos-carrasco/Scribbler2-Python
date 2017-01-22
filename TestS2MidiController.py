#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Demo de control del S2 desde MIDI."""

import mido

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils


def main():
    """Demo de control del S2 utilizando un controlador MIDI.

    Utiliza jackd a traves de la libreria Mido.

    """
    print( "Conectando a JACK" )
    mido.set_backend('mido.backends.rtmidi/UNIX_JACK')
    midiIn = mido.open_input( 'Scribbler2', virtual = True, autoreset = True  )

    print( "Conectando con el Scribbler2" )
    robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
    s2Motors = robot.getS2Motors()

    print( "Conecte la puerta del Controlador Midi a RTMidiInCient" )
    while( True ):
        cmd = None
        if( midiIn.pending() > 0 ):
            # .type, .channel, .note, .velocity, .time
            message = midiIn.receive()
            message.channel = message.channel + 1
            print( message )

            if( message.type == 'note_on' ):
                if( message.note == 36 ):
                    s2Motors.setMotors( 100, -100)
                elif( message.note == 37 ):
                    s2Motors.setMotors( -100, 100)
                elif( message.note == 40 ):
                    s2Motors.setMotors( 100, 100)
                elif( message.note == 41 ):
                    s2Motors.setMotors( -100, -100)
                elif( message.note == 43 ):
                    s2Motors.setMotorsOff()

    midiIn.close()
    robot.close()


if( __name__ == "__main__" ):
    main()
