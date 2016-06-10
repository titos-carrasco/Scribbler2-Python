# -*- coding: utf-8 -*-asco

""" Acceso a los LEDs de la F2

"""
class F2LEDs:
    def __init__( self, s2 ):
        self.s2 = s2

    def setBrightLed( self, pwm ):
        """ Establece potencia del Led de la F2

        Args:
            pwm (byte): potencia para el LED de la F2

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
