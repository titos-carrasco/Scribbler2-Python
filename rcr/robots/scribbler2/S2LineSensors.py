# -*- coding: utf-8 -*-

"""Acceso a los sensores de linea del S2."""

from .HS2LineSensors import HS2LineSensors

class S2LineSensors:
    """Clase de acceso a los sensores de linea del S2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def getLeftLine( self ):
        """
        Obtiene el valor del sensor de linea izquierdo.

        @rtype: integer
        @return: valor del sensor de linea izquierdo
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 74 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getRightLine( self ):
        """
        Obtiene el valor del sensor de linea derecho.

         @rtype: integer
         @return: valor del sensor de linea derecho
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 75 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getAllLines( self ):
        """
        Obtiene el valor de los sensores de linea del S2.

        @rtype: L{HS2LineSensors}
        @return: el valor de los sensores de linea del S2
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 76 )
            self.s2.sendS2Command( packet, 0 )
            return HS2LineSensors( self.s2.getUInt8Response(), self.s2.getUInt8Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getLineEx( self, side, thres):
        """
        Obtiene el valor extendido de un sensor de linea.

        @type side: integer
        @param side: el sensor de linea (0 o 1)
        @type thres: byte
        @param thres: umbral para la lectura del valor del sensor
        @rtype: integer
        @return: valor extendido del sensor de linea
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 173 )
            packet[1] = side & 0x01
            packet[2] = 0
            packet[3] = thres & 0xFF
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
