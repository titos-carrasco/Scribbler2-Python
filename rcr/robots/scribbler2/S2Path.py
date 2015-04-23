# -*- coding: utf-8 -*-

from HS2Coordinates import HS2Coordinates

class S2Path:
    def __init__( self, s2 ):
        self.s2 = s2

    def beginPath( self, speed ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 161 )
            packet[1] = 1
            packet[2] = 0
            packet[3] = speed & 0x0F
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def endPath( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 161 )
            packet[1] = 0
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getPosn( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 165 )
            self.s2.sendS2Command( packet, 0 )
            return HS2Coordinates( self.s2.getInt32Response(), self.s2.getInt32Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getAngle( self ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 167 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getInt32Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setPosn( self, x, y ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 166 )
            packet[1] = (x >> 24) & 0xFF
            packet[2] = (x >> 16) & 0xFF
            packet[3] = (x >> 8) & 0xFF
            packet[4] = x & 0xFF
            packet[5] = (y >> 24) & 0xFF
            packet[6] = (y >> 16) & 0xFF
            packet[7] = (y >> 8) & 0xFF
            packet[8] = y & 0xFF
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setAngle( self, angle ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 168 )
            packet[1] = (angle >> 24) & 0xFF
            packet[2] = (angle >> 16) & 0xFF
            packet[3] = (angle >> 8) & 0xFF
            packet[4] = angle & 0xFF
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def moveTo( self, x, y ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 162 )
            packet[1] = 2 + 1
            packet[2] = (x >> 8) & 0xFF
            packet[3] = x & 0xFF
            packet[4] = (y >> 8) & 0xFF
            packet[5] = y & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def moveBy( self, x, y ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 162 )
            packet[1] = 4 + 1
            packet[2] = (x >> 8) & 0xFF
            packet[3] = x & 0xFF
            packet[4] = (y >> 8) & 0xFF
            packet[5] = y & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def turnTo( self, angle ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 164 )
            packet[1] = 2 + 1
            packet[2] = (angle >> 8) & 0xFF
            packet[3] = angle & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def turnBy( self, angle ):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 164 )
            packet[1] = 4 + 1
            packet[2] = (angle >> 8) & 0xFF
            packet[3] = angle & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def arcTo( self, x, y, radius):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 163 )
            packet[1] = 2 + 1
            packet[2] = (x >> 8) & 0xFF
            packet[3] = x & 0xFF
            packet[4] = (y >> 8) & 0xFF
            packet[5] = y & 0xFF
            packet[6] = (radius >> 8) & 0xFF
            packet[7] = radius & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def arcBy( self, x, y, radius):
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 163 )
            packet[1] = 4 + 1
            packet[2] = (x >> 8) & 0xFF
            packet[3] = x & 0xFF
            packet[4] = (y >> 8) & 0xFF
            packet[5] = y & 0xFF
            packet[6] = (radius >> 8) & 0xFF
            packet[7] = radius & 0xFF
            self.s2.sendS2PathCommand( packet )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
