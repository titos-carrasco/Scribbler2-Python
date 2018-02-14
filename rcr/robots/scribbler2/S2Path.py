# -*- coding: utf-8 -*-

class S2Path:
    """Clase de acceso a las operaciones de PATH del S2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def beginPath( self, speed ):
        """
        Ingresa al modo de sistema cartesiano (path).

        @type speed: integer
        @param speed: velocidad de desplazamiento (0 a 15)
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Finaliza el modo path.

        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Obtiene ubicacion (x, y) del S2 en el plano cartesiano.

        @rtype: ( integer, integer )
        @return: coordenadas (x, y) de la ubicacion del S2
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 165 )
            self.s2.sendS2Command( packet, 0 )
            return ( self.s2.getInt32Response(), self.s2.getInt32Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getAngle( self ):
        """
        Obtiene angulo en el que se encuentra orientado el S2.

        @rtype: integer
        @return: angulo de orientacion del S2
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
        """
        Establece posicion (x, y) del S2 en el plano (no lo desplaza).

        @type x: integer
        @param x: coordenada X de la posicion
        @type y: integer
        @param y: coordenada Y de la posicion
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Establece angulo de orientacion del S2 (no lo desplaza).

        @type angle: integer
        @param angle: angulo de orientacion a fijar
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Desplaza el S2 a la posicion (x, y).

        @type x: integer
        @param x: coordenada X hacia donde desplazar
        @type y: integer
        @param y: coordenada Y hacia donde desplazar
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Desplaza de manera relativa el S2 una distancia (x, y).

        @type x: integer
        @param x: distancia e X a desplazar al S2
        @type y: integer
        @param y: distancia en Y a desplazar al S2
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Mueve al S2 orientandolo a un angulo dado.

        @type angle: integer
        @param angle: angulo hacia el cual mover el S2
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Gira de manera relativa el S2 un numero dado de grados.

        @type angle: integer
        @param angle: grados a girar el S2 segun prientacion actual
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Traza un arco hasta la posicon (x, y) de radio dado.

        @type x: integer
        @param x: coordenada X hacia la cual desplazar
        @type y: integer
        @param y: coordenada Y hacia la cual desplazar
        @type radius: integer
        @param radius: radio de arco a trazar
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Traza un arco de manera relativa y de radio dado.

        @type x: integer
        @param x: pasos en X a desplazar segun posicion actual
        @type y: integer
        @param y: pasos en Y a desplazar segun posicion actual
        @type radius: integer
        @param radius: radio de arco a trazar
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
