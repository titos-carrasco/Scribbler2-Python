# -*- coding: utf-8 -*-

""" Acceso a los sensores de línea del S2

"""
from .HS2LineSensors import HS2LineSensors

class S2LineSensors:
    def __init__( self, s2 ):
        self.s2 = s2

    def getLeftLine( self ):
        """ Obtiene el valor del sensor de línea izquierdo

        Returns:
            int: valor del sensor de línea izquierdo

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
        """ Obtiene el valor del sensor de línea derecho

        Returns:
            int: valor del sensor de línea derecho

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
        """ Obtiene el valor de los sensores de línea del S2

        Returns:
            HS2LineSensor: el valor de los sensores de línea del S2

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
        """ Obtiene el valor extendido de un sensor de línea

        Args:
            side (int): el sensor de línea (0 o 1)
            thres (byte): umbral para la lectura del valor del sensor

        Returns:
            int: valor extendido del sensor de línea

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
