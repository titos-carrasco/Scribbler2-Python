# -*- coding: utf-8 -*-

"""Acceso al parlante del S2."""

class S2Speaker:
    """Clase de acceso al parlante del S2."""

    def __init__( self, s2 ):
        """Constructor de la clase.

        Args:
            s2 (Scribber2): referencia al S2

        """
        self.s2 = s2

    def setQuiet( self ):
        """Apaga el parlante del S2.

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

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
        """Activa el parlante del S2.

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

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
        """Establece porcentaje del nivel de volumen del parlante del S2.

        Args:
            volume (int): porcentaje de volumen (0 a 100) del parlante

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

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
        """Emite sonido a traves del parlante del S2.

        Args:
            duration (int): durancion del sonido en ms (no superior a 2500)
            freq1 (int): frecuencia principal en Hz
            freq2 (int): frecuencia secundaria en Hz

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

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
