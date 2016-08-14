# -*- coding: utf-8 -*-

"""Acceso al conector de servos de la F2."""

from rcr.utils import Utils

class F2Servos:
    """Clase de acceso a los motores servos de la F2."""

    def __init__( self, s2 ):
        """Constructor de la clase.

        Args:
            s2 (Scribber2): referencia al S2

        """
        self.s2 = s2

    def setServo( self, id, value ):
        """Establece valor al servo conectado a la F2.

        Args:
            id (byte): servo a utilizar (0 a 3)
            value (byte): valor a enviar

        """
        try:
            self.s2.lock()
            packet = bytearray( 3 )
            packet[0] = 12
            packet[1] = id & 0x03
            packet[2] = value & 0xFF
            self.s2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
