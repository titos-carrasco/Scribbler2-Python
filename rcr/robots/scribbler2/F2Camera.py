# -*- coding: utf-8 -*-

from HF2Image import HF2Image

class F2Camera:
    IMAGE_LARGE = 1
    IMAGE_SMALL = 2
    IMAGE_GRAYJPEG = 1
    IMAGE_GRAYJPEG_FAST = 2
    IMAGE_JPEG  = 3
    IMAGE_JPEG_FAST = 4

    def __init__( self, s2 ):
        self.image_width  = 0
        self.image_height = 0
        self.s2 = s2

    def setPicSize( self, size ):
        try:
            self.s2.lock()
            if( size == self.IMAGE_LARGE ):
                s = 213
                w = 1280
                h = 800
            else: # if( size == self.IMAGE_SMALL )
                s = 71
                w = 427
                h = 266
            packet = bytearray( 2 )
            packet[0] = 11
            packet[1] = s
            self.s2.sendF2Command( packet, 100 )
            self.image_width = w
            self.image_height = h
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getImage( self, mode ):
        try:
            self.s2.lock()
            if( mode == self.IMAGE_GRAYJPEG ):
                reg = 1
                cmd_header = 135
                cmd = 136
            elif( mode == self.IMAGE_GRAYJPEG_FAST ):
                reg = 0
                cmd_header = 135
                cmd = 136
            elif( mode == self.IMAGE_JPEG ):
                reg = 1
                cmd_header = 137
                cmd = 138
            else: # if( mode == self.IMAGE_JPEG_FAST )
                reg = 0
                cmd_header = 137
                cmd = 138
            packet = bytearray(1)
            packet[0] = cmd_header
            self.s2.sendF2Command( packet, 100 )

            header_len = self.s2.getUInt8Response() + (self.s2.getUInt8Response() << 8)
            image = self.s2.getBytesResponse( header_len )

            packet = bytearray( 2 )
            packet[0] = cmd
            packet[1] = reg
            self.s2.sendF2Command( packet, 100 )

            last = 0x00
            while( True ):
                b = self.s2.getUInt8Response()
                image.append( b )
                if( b == 0xD9 and last == 0xFF):
                    self.s2.getUInt32Response()
                    self.s2.getUInt32Response()
                    self.s2.getUInt32Response()
                    break
                last = b
            return HF2Image( self.image_width, self.image_height, image )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def whiteBalanceOn( self ):
        try:
            self.s2.lock()
            packet = bytearray( 1 )
            packet[0] = 129
            self.s2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def whiteBalanceOff( self ):
        try:
            self.s2.lock()
            packet = bytearray( 1 )
            packet[0] = 130
            self.s2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setCameraParam( self, addr, value ):
        try:
            self.s2.lock()
            packet = bytearray( 3 )
            packet[0] = 131
            packet[1] = addr & 0xFF
            packet[2] = value & 0xFF
            self.s2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setWindow( self, window, xLow, yLow, xHigh, yHigh, xStep, yStep ):
        try:
            self.s2.lock()
            packet = bytearray( 12 )
            packet[0] = 127
            packet[1] = window & 0xFF
            packet[2] = (xLow >> 8) & 0xFF
            packet[3] = xLow & 0xFF
            packet[4] = (yLow >> 8) & 0xFF
            packet[5] = yLow & 0xFF
            packet[6] = (xHigh >> 8) & 0xFF
            packet[7] = xHigh & 0xFF
            packet[8] = (yHigh >> 8) & 0xFF
            packet[9] = yHigh & 0xFF
            packet[10] = xStep & 0xFF
            packet[11] = yStep & 0xFF
            s2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
