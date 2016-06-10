# -*- coding: utf-8 -*-

""" Acceso al módulo de movimiento por rutas (path - plano cartesiano)

"""
from .HS2Coordinates import HS2Coordinates

class S2Path:
    def __init__( self, s2 ):
        self.s2 = s2

    def beginPath( self, speed ):
        """ Ingresa al modo de sistema cartesiano (path)

        Args:
            speed (int): velocidad de desplazamiento (0 a 15)

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 161 )
            packet[1] = 1
            packet[2] = 0
            packet[3] = speed & 0x0F
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def endPath( self ):
        """ Finaliza el modo path

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 161 )
            packet[1] = 0
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getPosn( self ):
        """ Obtiene ubicación (x, y) del S2 en el plano cartesiano

        Returns:
            HS2Coordinates: coordenadas de la ubización del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 165 )
            self.s2.sendS2Command( packet, 0 )
            return HS2Coordinates( self.s2.getInt32Response(), self.s2.getInt32Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getAngle( self ):
        """ Obtiene ángulo en el que se encuentra orientado el S2

        Returns:
            int: ángulo de orientación del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 167 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getInt32Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setPosn( self, x, y ):
        """ Establece posición (x, y) del S2 en el plano (no lo desplaza)

        Args:
            x (int): coordenada X de la posición
            y (int): coordenada Y de la posición

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 166 )
            packet[1] = (x >> 24) & 0xFF
            packet[2] = (x >> 16) & 0xFF
            packet[3] = (x >> 8) & 0xFF
            packet[4] = x & 0xFF
            packet[5] = (y >> 24) & 0xFF
            packet[6] = (y >> 16) & 0xFF
            packet[7] = (y >> 8) & 0xFF
            packet[8] = y & 0xFF
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setAngle( self, angle ):
        """ Establece ángulo de orientación del S2 (no lo desplaza)

        Args:
            angle (int): ángulo de orientación a fijar

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 168 )
            packet[1] = (angle >> 24) & 0xFF
            packet[2] = (angle >> 16) & 0xFF
            packet[3] = (angle >> 8) & 0xFF
            packet[4] = angle & 0xFF
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def moveTo( self, x, y ):
        """ Desplaza el S2 a la posición (x, y)

        Args:
            x (int): coordenada X hacia donde desplazar
            y (int): coordenada Y hacia donde desplazar

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 162 )
            packet[1] = 2 + 1
            packet[2] = (x >> 8) & 0xFF
            packet[3] = x & 0xFF
            packet[4] = (y >> 8) & 0xFF
            packet[5] = y & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def moveBy( self, x, y ):
        """ Desplaza de manera relativa el S2 una distancia (x, y)

        Args:
            x (int): distancia e X a desplazar al S2
            y (int): distancia en Y a desplazar al S2

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 162 )
            packet[1] = 4 + 1
            packet[2] = (x >> 8) & 0xFF
            packet[3] = x & 0xFF
            packet[4] = (y >> 8) & 0xFF
            packet[5] = y & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def turnTo( self, angle ):
        """ Mueve al S2 orientándolo a un ángulo dado

        Args:
            angle (int): ángulo hacia el cual mover el S2

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 164 )
            packet[1] = 2 + 1
            packet[2] = (angle >> 8) & 0xFF
            packet[3] = angle & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def turnBy( self, angle ):
        """ Gira de manera relativa el S2 un número dado de grados

        Args:
            angle (int): grados a girar el S2 según prientación actual

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 164 )
            packet[1] = 4 + 1
            packet[2] = (angle >> 8) & 0xFF
            packet[3] = angle & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def arcTo( self, x, y, radius):
        """ Traza un arco hasta la posicón (x, y) de radio dado

        Args:
            x (int): coordenada X hacia la cual desplazar
            y (int): coordenada Y hacia la cual desplazar
            radio (int): radio de arco a trazar

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 163 )
            packet[1] = 2 + 1
            packet[2] = (x >> 8) & 0xFF
            packet[3] = x & 0xFF
            packet[4] = (y >> 8) & 0xFF
            packet[5] = y & 0xFF
            packet[6] = (radius >> 8) & 0xFF
            packet[7] = radius & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def arcBy( self, x, y, radius):
        """ Traza un arco de manera relativa y de radio dado

        Args:
            x (int): pasos en X a desplazar según posición actual
            y (int): pasos en Y a desplazar según posición actual
            radio (int): radio de arco a trazar

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 163 )
            packet[1] = 4 + 1
            packet[2] = (x >> 8) & 0xFF
            packet[3] = x & 0xFF
            packet[4] = (y >> 8) & 0xFF
            packet[5] = y & 0xFF
            packet[6] = (radius >> 8) & 0xFF
            packet[7] = radius & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
