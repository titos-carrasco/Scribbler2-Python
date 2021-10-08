# -*- coding: utf-8 -*-

"""Acceso a los sensores infrarojos de la F2."""

class F2IRSensors:
    """Clase de acceso a los sensores infrarojos de la F2."""

    def __init__( self, f2 ):
        """
        Corresponde al constructor de la clase.

        @type f2: L{Fluke2}
        @param f2: referencia a la F2 que lo contiene
        """
        self.f2 = f2

    def setIRPower( self,  pwm ):
        """
        Establece energia para el sensor IR.

        @type pwm: byte
        @param pwm: energia para el sensor IR de la F2
        """
        try:
            self.f2.lock()
            packet = bytearray( 2 )
            packet[0] = 120
            packet[1] = pwm & 0xFF
            self.f2.sendF2Command( packet, 0.1 )
        except Exception as e:
            raise
        finally:
            self.f2.unlock()

    def getIR( self ):
        """
        Obtiene valor del sensor IR de la F2.

        @rtype: integer
        @return: valor del sensor IR de la F2
        """
        try:
            self.f2.lock()
            packet = bytearray( 1 )
            packet[0] = 86
            self.f2.sendF2Command( packet, 0.1 )
            return self.f2.getUInt16Response()
        except Exception as e:
            raise
        finally:
            self.f2.unlock()
