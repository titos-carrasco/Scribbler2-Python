# -*- coding: utf-8 -*-asco

"""Acceso a los LEDs de la F2."""

class F2LEDs:
    """Clase de acceso a los LEDs del F2."""

    def __init__( self, f2 ):
        """
        Corresponde al constructor de la clase.

        @type f2: L{Fluke2}
        @param f2: referencia a la F2 que lo contiene
        """
        self.f2 = f2

    def setBrightLed( self, pwm ):
        """
        Establece potencia del Led de la F2.

        @type pwm: byte
        @param pwm: potencia para el LED de la F2
        """
        try:
            self.f2.lock()
            packet = bytearray( 2 )
            packet[0] = 126
            packet[1] = pwm & 0xFF
            self.f2.sendF2Command( packet, 0.1 )
        except Exception as e:
            raise
        finally:
            self.f2.unlock()
