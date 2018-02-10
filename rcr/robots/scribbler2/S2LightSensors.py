# -*- coding: utf-8 -*-

"""Acceso a los sensores de luz del S2."""

from .HS2Lights import HS2Lights

class S2LightSensors:
    """Clase de acceso a los sensores de luz del S2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def getLeftLight( self ):
        """
        Obtiene el valor del sensor de luz izquierdo.

        @rtype: integer
        @return: valor del sensor de luz izquierdo
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 67 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt16Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getCenterLight( self ):
        """
        Obtiene el valor del sensor de luz central.

        @rtype: integer
        @return: valor del sensor de luz central
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 68 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt16Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getRightLight( self ):
        """
        Obtiene el valor del sensor de luz derecho.

        @rtype: integer
        @return: valor del sensor de luz derecho
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 69 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt16Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getAllLights( self ):
        """
        Obtiene el valor de los sensores de luz.

        @rtype: L{HS2Lights}
        @return: valor de los sensores de luz del S2
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 70 )
            self.s2.sendS2Command( packet, 0 )
            return HS2Lights( self.s2.getUInt16Response(), self.s2.getUInt16Response(), self.s2.getUInt16Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
