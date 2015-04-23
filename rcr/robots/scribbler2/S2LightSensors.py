# -*- coding: utf-8 -*-

from HS2Lights import HS2Lights

class S2LightSensors:
    def __init__( self, s2 ):
        self.s2 = s2

    def getLeftLight( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 67 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt16Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getCenterLight( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 68 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt16Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getRightLed( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 69 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt16Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getAllLights( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 70 )
            self.s2.sendS2Command( packet, 0 )
            return HS2Lights( self.s2.getUInt16Response(), self.s2.getUInt16Response(), self.s2.getUInt16Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
