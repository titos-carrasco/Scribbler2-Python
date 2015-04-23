# -*- coding: utf-8 -*-

class S2Microphone:
    def __init__( self, s2 ):
        self.s2 = s2

    def getMicEnv( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 169 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt32Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
