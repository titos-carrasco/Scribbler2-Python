# -*- coding: utf-8 -*-

class F2IRSensors:
    def __init__( self, s2 ):
        self.s2 = s2

    def setIRPower( self,  pwm ):
        try:
            self.s2.lock()
            packet = bytearray( 2 )
            packet[0] = 120
            packet[1] = pwm & 0xFF
            self.s2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getIR( self ):
        try:
            self.s2.lock()
            packet = bytearray( 1 )
            packet[0] = 86
            self.s2.sendF2Command( packet, 100 )
            return self.s2.getUInt16Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
