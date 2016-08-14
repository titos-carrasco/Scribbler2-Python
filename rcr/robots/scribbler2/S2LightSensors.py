# -*- coding: utf-8 -*-

"""Acceso a los sensores de luz del S2."""

from .HS2Lights import HS2Lights

class S2LightSensors:
    """Clase de acceso a los sensores de luz del S2."""

    def __init__( self, s2 ):
        """Constructor de la clase.

        Args:
            s2 (Scribber2): referencia al S2

        """
        self.s2 = s2

    def getLeftLight( self ):
        """Obtiene el valor del sensor de luz izquierdo.

        Returns:
            int: valor del sensor de luz izquierdo

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
        """Obtiene el valor del sensor de luz central.

        Returns:
            int: valor del sensor de luz central

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

    def getRightLed( self ):
        """Obtiene el valor del sensor de luz derecho.

        Returns:
            int: valor del sensor de luz derecho

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
        """Obtiene el valor de los sensores de luz.

        Returns:
            HS2Lights: valor de los sensores de luz del S2

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
