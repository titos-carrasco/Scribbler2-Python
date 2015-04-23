# -*- coding: utf-8 -*-

from HS2Infrared import HS2Infrared

class S2IRSensors:
    def __init__( self, s2 ):
        self.s2 = s2

    def getIRLeft( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 71 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getIRRight( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 72 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getAllIR( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 73 )
            self.s2.sendS2Command( packet, 0 )
            return HS2Infrared( self.s2.getUInt8Response(), self.s2.getUInt8Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getIrEx( self, side, thres):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 172 )
            packet[1] = side & 0x01
            packet[2] = 0
            packet[3] = thres & 0xFF
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getDistanceEx( self, side ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 175 )
            packet[1] = side & 0x01
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
