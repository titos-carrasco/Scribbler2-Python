# -*- coding: utf-8 -*-

"""Acceso al parlante del S2."""

class S2Speaker:
    """Clase de acceso al parlante del S2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def setQuiet( self ):
        """
        Apaga el parlante del S2.

        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 112 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setLoud( self ):
        """
        Activa el parlante del S2.

        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 111 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setVolume( self, volume ):
        """
        Establece porcentaje del nivel de volumen del parlante del S2.

        @type volume: integer
        @param volume: porcentaje de volumen (0 a 100) del parlante
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
        """
        try:
            self.s2.lock()
            volume = volume & 0xFF
            if( volume > 100 ):
                volume= 100
            packet = self.s2.makeS2Packet( 160 )
            packet[1] = volume
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setSpeaker( self, duration, freq1, freq2):
        """
        Genera sonido a traves del parlante del S2.

        @type duration: integer
        @param duration: duracion del sonido en ms (no superior a 2500)
        @type freq1: integer
        @param freq1: frecuencia principal en Hz
        @type freq2: integer
        @param freq2: frecuencia secundaria en Hz
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
        """
        try:
            self.s2.lock()
            duration = duration & 0xFFFF
            if( duration > 2500 ):
                duration = 2500
            freq1 = freq1 & 0xFFFF
            freq2 = freq2 & 0xFFFF
            packet = self.s2.makeS2Packet( 114 )
            packet[1] = (duration >>8) & 0xFF
            packet[2] = duration & 0xFF
            packet[3] = (freq1 >> 8) & 0xFF
            packet[4] = freq1 & 0xFF
            packet[5] = (freq2 >> 8) & 0xFF
            packet[6] = freq2 & 0xFF
            self.s2.sendS2Command( packet, duration )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
