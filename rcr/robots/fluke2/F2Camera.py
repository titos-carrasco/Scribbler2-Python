# -*- coding: utf-8 -*-

"""Acceso a la camara del F2."""

from .HF2Image import HF2Image

class F2Camera:
    """Clase de acceso a la camara de la F2."""

    IMAGE_LARGE = 1
    IMAGE_SMALL = 2
    IMAGE_GRAYJPEG = 1
    IMAGE_GRAYJPEG_FAST = 2
    IMAGE_JPEG  = 3
    IMAGE_JPEG_FAST = 4

    def __init__( self, f2 ):
        """
        Corresponde al constructor de la clase.

        @type f2: L{Fluke2}
        @param f2: referencia a la F2 que lo contiene
        """
        self.image_width  = 0
        self.image_height = 0
        self.f2 = f2

    def setPicSize( self, size ):
        """
        Establece tamano de la imagen a capturar desde la F2.

        @type size: integer
        @param size: tamano y formato de la imagen
            - F2Camera.IMAGE_LARGE: 1280x800
            - F2Camera.IMAGE_SMALL: 427x266
        """
        try:
            self.f2.lock()
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
            self.f2.sendF2Command( packet, 100 )
            self.image_width = w
            self.image_height = h
        except Exception as e:
            raise
        finally:
            self.f2.unlock()

    def getImage( self, mode ):
        """
        Captura imagen desde la F2 especificando formato.

        @type mode: integer
        @param mode: formato de la imagen:
                - F2Camera.IMAGE_GRAYJPEG - tonos de gris
                - F2Camera.IMAGE_GRAYJPEG_FAST - tonos de gris
                - F2Camera.IMAGE_JPEG - color
                - F2Camera.IMAGE_JPEG_FAST - color
        @rtype: bytearray
        @return: la imagen capturada
        """
        try:
            self.f2.lock()
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
            self.f2.sendF2Command( packet, 100 )

            header_len = self.f2.getUInt8Response() + (self.f2.getUInt8Response() << 8)
            image = self.f2.getBytesResponse( header_len )

            packet = bytearray( 2 )
            packet[0] = cmd
            packet[1] = reg
            self.f2.sendF2Command( packet, 100 )

            last = 0x00
            while( True ):
                b = self.f2.getUInt8Response()
                image.append( b )
                if( b == 0xD9 and last == 0xFF):
                    self.f2.getUInt32Response()
                    self.f2.getUInt32Response()
                    self.f2.getUInt32Response()
                    break
                last = b
            return HF2Image( self.image_width, self.image_height, image )
        except Exception as e:
            raise
        finally:
            self.f2.unlock()

    def whiteBalanceOn( self ):
        """Activa balance de blancos."""
        try:
            self.f2.lock()
            packet = bytearray( 1 )
            packet[0] = 129
            self.f2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.f2.unlock()

    def whiteBalanceOff( self ):
        """Desactiva balance de blancos."""
        try:
            self.f2.lock()
            packet = bytearray( 1 )
            packet[0] = 130
            self.f2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.f2.unlock()

    def setCameraParam( self, addr, value ):
        """
        Establece parametros especificos para la camara del F2.

        @type addr: byte
        @param addr: ¿?
        @type value: byte
        @param value: ¿?
        """
        try:
            self.f2.lock()
            packet = bytearray( 3 )
            packet[0] = 131
            packet[1] = addr & 0xFF
            packet[2] = value & 0xFF
            self.f2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.f2.unlock()

    def setWindow( self, window, xLow, yLow, xHigh, yHigh, xStep, yStep ):
        """
        Establece parametros de la ventana de captura.

        @type window: integer
        @param window: ¿?
        @type xLow: integer
        @param xLow: ¿?
        @type yLow: integer
        @param yLow: ¿?
        @type xHigh: integer
        @param xHigh: ¿?
        @type yHigh: integer
        @param yHigh: ¿?
        @type xStep: integer
        @param xStep: ¿?
        @type yStep: integer
        @param yStep: ¿?
        """
        try:
            self.f2.lock()
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
            self.f2.sendF2Command( packet, 100 )
        except Exception as e:
            raise
        finally:
            self.f2.unlock()
