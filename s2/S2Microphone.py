# -*- coding: utf-8 -*-

"""Acceso al microfono del S2."""

class S2Microphone:
    """Clase de acceso al microfono del S2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def getMicEnv( self ):
        """
        Obtiene el valor del microfono del S2.

        @rtype: integer
        @return: valor del microfono del S2
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 169 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt32Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
