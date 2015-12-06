# -*- coding: utf-8 -*-

from rcr.utils import Utils

class F2Servos:
    def __init__( self, s2 ):
        self.s2 = s2

    def setServo( self, id, value ):
        try:
            self.s2.lock()
            packet = bytearray( 3 )
            packet[0] = 12
            packet[1] = id & 0x03
            packet[2] = value & 0xFF
            self.s2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
