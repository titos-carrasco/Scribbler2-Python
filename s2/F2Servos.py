# -*- coding: utf-8 -*-

"""Acceso al conector de servos de la F2."""

class F2Servos:
    """Clase de acceso a los motores servos de la F2."""

    def __init__( self, f2 ):
        """
        Corresponde al constructor de la clase.

        @type f2: L{Fluke2}
        @param f2: referencia a la F2 que lo contiene
        """
        self.f2 = f2

    def setServo( self, id, value ):
        """
        Establece valor al servo conectado a la F2.

        @type id: byte
        @param id: servo a utilizar (0 a 3)
        @type value: byte
        @param value: valor a enviar
        """
        try:
            self.f2.lock()
            packet = bytearray( 3 )
            packet[0] = 12
            packet[1] = id & 0x03
            packet[2] = value & 0xFF
            self.f2.sendF2Command( packet, 0.1 )
        except Exception as e:
            raise
        finally:
            self.f2.unlock()
