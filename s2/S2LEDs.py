# -*- coding: utf-8 -*-

"""Acceso a los LEDs del S2."""

class S2LEDs:
    """Clase de acceso a los LEDs del S2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def setLeftLed( self, encender ):
        """
        Enciende o apaga el LED izquierdo.

        @type encender: bool
        @param encender: orden de apagar o encender el LED
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Enciende o apaga el LED central.

        @type encender: bool
        @param encender: orden de apagar o encender el LED
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Enciende o apaga el LED derecho.

        @type encender: bool
        @param encender: orden de apagar o encender el LED
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Enciende o apaga los LEDs del S2.

        @type left: bool
        @param left: orden de apagar o encender el LED izquierdo
        @type center: bool
        @param center: orden de apagar o encender el LED central
        @type right: bool
        @param right: orden de apagar o encender el LED derecho
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
