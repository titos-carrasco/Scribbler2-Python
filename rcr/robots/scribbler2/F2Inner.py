# -*- coding: utf-8 -*-

""" Acceso a los datos internos de la F2

"""
from rcr.utils import Utils

class F2Inner:
    FLUKE_FORWARD = 1
    SCRIBBLER_FORWARD = 2

    def __init__( self, s2 ):
        self.s2 = s2

    def getVersion( self ):
        """ Obtiene versión de la F2

        Returns:
            str: versión de la F2
        """
        try:
            self.s2.lock()
            packet = bytearray(1)
            packet[0] = 142
            self.s2.sendF2Command( packet, 100 )
            return self.s2.getLineResponse( 128 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def identifyRobot( self ):
        """ Obtiene infromación que identifica al S2

        Returns:
            str: identifiación del S2

        """
        try:
            self.s2.lock()
            packet = bytearray( 1 )
            packet[0] = 156
            self.s2.sendF2Command( packet, 100 )
            id = self.s2.getLineResponse( 128 )
            Utils.pause( 4000 )
            return id
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getBattery( self ):
        """ Obtiene voltaje de la batería

        Returns:
            float: voltaje de la batería

        """
        try:
            self.s2.lock()
            packet = bytearray( 1 )
            packet[0] = 89
            self.s2.sendF2Command( packet, 100 )
            return self.s2.getUInt16Response() / 20.9813
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setForwardness( self, forwardness ):
        """ Establece cual es el frente del S2 para ciertos comandos

        Args:
            forwardness (byte): frente del S2:
                F2inner.FLUKE_FORWARD: la tarjeta F2 es el frente
                F2inner.SCRIBBLER_FORWARD: los sensores de luz son el frente

        """
        try:
            self.s2.lock()
            if( forwardness == self.FLUKE_FORWARD):
                f = 0
            else: # if( forwardness == self.SCRIBBLER_FORWARD )
                f = 1
            packet = bytearray( 2 )
            packet[0] = 128
            packet[1] = f
            self.s2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getErrors( self ):
        """ Obtiene el log de errores almacenados en la F2

        Returns:
            str: líneas del texto del log de errores

        """
        try:
            self.s2.lock()
            packet = bytearray( 1 )
            packet[0] = 10
            self.s2.sendF2Command( packet, 100 )
            n = self.s2.getUInt16Response()
            log = self.s2.getBytesResponse( n )
            return log.decode('ascii')
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def resetScribbler( self ):
        """ Resetea el S2

        """
        try:
            self.s2.lock()
            packet = bytearray( 1 )
            packet[0] = 124
            self.s2.sendF2Command( packet, 100 )
            Utils.pause( 4000 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
