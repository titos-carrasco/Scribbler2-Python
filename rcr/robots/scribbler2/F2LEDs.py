# -*- coding: utf-8 -*-asco

"""Acceso a los LEDs de la F2."""

class F2LEDs:
    """Clase de acceso a los LEDs del F2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def setBrightLed( self, pwm ):
        """
        Establece potencia del Led de la F2.

        @type pwm: byte
        @param pwm: potencia para el LED de la F2
        """
        try:
            self.s2.lock()
            packet = bytearray( 2 )
            packet[0] = 126
            packet[1] = pwm & 0xFF
            self.s2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
