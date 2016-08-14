# -*- coding: utf-8 -*-

"""Acceso a los LEDs del S2."""

class S2LEDs:
    """Clase de acceso a los LEDs del S2."""

    def __init__( self, s2 ):
        """Constructor de la clase.

        Args:
            s2 (Scribber2): referencia al S2

        """
        self.s2 = s2

    def setLeftLed( self, encender ):
        """Enciende o apaga el LED izquierdo.

        Args:
            encender (bool): orden de apagar o encender el LED

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            cmd = 100
            if( encender ):
                cmd = 99
            packet = self.s2.makeS2Packet( cmd )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setCenterLed( self, encender ):
        """Enciende o apaga el LED central.

        Args:
            encender (bool): orden de apagar o encender el LED

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            cmd = 102
            if( encender ):
                cmd = 101
            packet = self.s2.makeS2Packet( cmd )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setRightLed( self, encender ):
        """Enciende o apaga el LED derecho.

        Args:
            encender (bool): orden de apagar o encender el LED

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            cmd = 104
            if( encender ):
                cmd = 103
            packet = self.s2.makeS2Packet( cmd )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setAllLed( self, left, center, right ):
        """Enciende o apaga los LEDs del S2.

        Args:
            left (bool): orden de apagar o encender el LED izquierdo
            center (bool): orden de apagar o encender el LED central
            right (bool): orden de apagar o encender el LED derecho

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 107 )
            packet[1] = left & 0x01
            packet[2] = center & 0x01
            packet[3] = right & 0x01
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
