# -*- coding: utf-8 -*-

"""Acceso a los sensores infrarojos de la F2."""

class F2IRSensors:
    """Clase de acceso a los sensores infrarojos de la F2."""

    def __init__( self, s2 ):
        """Constructor de la clase.

        Args:
            s2 (Scribber2): referencia al S2

        """
        self.s2 = s2

    def setIRPower( self,  pwm ):
        """Establece energia para el sensor IR.

        Args:
            pwm (byte): energia para el sensor IR de la F2

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
        """Obtiene valor del sensor IR de la F2.

        Returns:
            int: valor del sensor IR de la F2

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
