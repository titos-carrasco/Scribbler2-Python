# -*- coding: utf-8 -*-

class S2LEDs:
    def __init__( self, s2 ):
        self.s2 = s2

    def setLeftLed( self, encender ):
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
