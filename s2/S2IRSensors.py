# -*- coding: utf-8 -*-

"""Acceso a los sensores IR del S2."""

from s2.HS2Infrared import HS2Infrared

class S2IRSensors:
    """Clase de acceso a los sensores infrarojos del S2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def getIRLeft( self ):
        """
        Obtiene valor del sensor IR izquierdo.

        @rtype: integer
        @return: valor del sensor IR izquierdo
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 71 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getIRRight( self ):
        """
        Obtiene valor del sensor IR derecho.

        @rtype: integer
        @return: valor del sensor IR derecho
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 72 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getAllIR( self ):
        """
        Obtiene el valor de todos los sensores IR del S2.

        @rtype: L{HS2Infrared}
        @return: el valor de los sensores IR del S2
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 73 )
            self.s2.sendS2Command( packet, 0 )
            return HS2Infrared( self.s2.getUInt8Response(), self.s2.getUInt8Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getIrEx( self, side, thres):
        """
        Obtiene el valor extendido de un sensor infrarojo del S2.

        @type side: byte
        @param side: el sensor a leer (0 o 1)
        @type thres: byte
        @param thres: el umbral a utilizar en la lectura
        @rtype: integer
        @return: valor del sensor leido
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 172 )
            packet[1] = side & 0x01
            packet[2] = 0
            packet[3] = thres & 0xFF
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getDistanceEx( self, side ):
        """
        Obtiene distacia medida por un sensor.

        @type side: integer
        @param side: sensor a utilizar (0 o 1)
        @rtype: integer
        @return: la distancia medida
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 175 )
            packet[1] = side & 0x01
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
