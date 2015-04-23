# -*- coding: utf-8 -*-

from HS2MotorStats import HS2MotorStats
from HS2Encoders import HS2Encoders

class S2Motors:
    def __init__( self, s2 ):
        self.s2 = s2

    def getMotorStats( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 170 )
            self.s2.sendS2Command( packet, 0 )
            return HS2MotorStats( self.s2.getUInt32Response(), self.s2.getUInt8Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getEncoders( self, preserve ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 171 )
            packet[1] = preserve & 0x01
            self.s2.sendS2Command( packet, 0 )
            return HS2Encoders( self.s2.getUInt32Response(), self.s2.getUInt32Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getStall( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 79 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setMotorsOff( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 108 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setMotors( self, left, right):
        try:
            self.s2.lock()
            if(left>100):
                left = 100
            elif(left<-100):
                left = -100
            left = left + 100

            if(right>100):
                right = 100
            elif(right<-100):
                right = -100
            right = right + 100

            packet = self.s2.makeS2Packet( 109 )
            packet[1] = right
            packet[2] = left
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
