# -*- coding: utf-8 -*-

from HS2LineSensors import HS2LineSensors

class S2LineSensors:
    def __init__( self, s2 ):
        self.s2 = s2

    def getLeftLine( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 74 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getRightLine( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 75 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getAllLines( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 76 )
            self.s2.sendS2Command( packet, 0 )
            return HS2LineSensors( self.s2.getUInt8Response(), self.s2.getUInt8Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getLineEx( self, side, thres):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 173 )
            packet[1] = side & 0x01
            packet[2] = 0
            packet[3] = thres & 0xFF
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
