# -*- coding: utf-8 -*-

"""Acceso a los sensores infrarojos de la F2."""

class F2IRSensors:
    """Clase de acceso a los sensores infrarojos de la F2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def setIRPower( self,  pwm ):
        """
        Establece energia para el sensor IR.

        @type pwm: byte
        @param pwm: energia para el sensor IR de la F2
        """
        try:
            self.s2.lock()
            packet = bytearray( 2 )
            packet[0] = 120
            packet[1] = pwm & 0xFF
            self.s2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getIR( self ):
        """
        Obtiene valor del sensor IR de la F2.

        @rtype: integer
        @return: valor del sensor IR de la F2
        """
        try:
            self.s2.lock()
            packet = bytearray( 1 )
            packet[0] = 86
            self.s2.sendF2Command( packet, 100 )
            return self.s2.getUInt16Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
