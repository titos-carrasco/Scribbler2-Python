# -*- coding: utf-8 -*-

"""Acceso a puerta serial."""

import serial
import time
from .SerialInterface import SerialInterface
from . import Utils

class Serial( SerialInterface ):
    """Clase para interactuar con puerta serial."""

    def __init__( self, port, bauds, timeout ):
        """
        Conecta a la puerta serial.

        @type port: string
        @param port: puerta serial de conexion
        @type bauds: integer
        @param bauds: velocidad de comunicacion
        @type timeout: integer
        @param timeout: timeout en milisegundos
        """
        super( Serial, self ).__init__()

        self.maxTries = timeout
        try:
            self.serial = serial.Serial(port, baudrate=bauds, bytesize=8,
                                       parity='N', stopbits=1,
                                       timeout=0 )
            self.serial.flushInput()
            self.serial.flushOutput()
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise

    def close( self ):
        """Finaliza la conexion con la puerta serial."""
        try:
            self.lock()
            self.serial.close()
            self.serial = None
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def write( self, dataBytes ):
        """
        Envia bytes por la puerta serial.

        @type dataBytes: byte, bytearray o equivalente
        @param dataBytes: bytes a enviar por la puerta serial
        """
        try:
            self.lock()
            self.serial.write( dataBytes )
            self.serial.flush()
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def read( self, nbytes ):
        """
        Lee bytes desde la puerta serial.

        @type nbytes: integer
        @param nbytes: numero de bytes a leer
        @rtype: bytearray
        @return: los bytes leidos
        @raise TimeoutException: si no se pudieron leer los bytes solicitados en el tiempo senalado
        """
        try:
            self.lock()
            dataBytes = bytearray( nbytes )
            pos = 0
            tries = 0
            while( pos < nbytes and tries < self.maxTries ):
                b = self.serial.read( 1 )
                if( len( b )==0 ):
                    Utils.pause( 1 )
                    tries = tries + 1
                    continue
                if( type( b ) is str ):
                    dataBytes[pos] = ord(b)
                else:
                    dataBytes[pos] = b[0]
                pos = pos + 1
                tries = 0
            if( pos < nbytes ):
                raise self.TimeoutException
            return dataBytes
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def readLine( self, maxChars ):
        """
        Lee una linea de texto finalizada en NL o del tamano especificado desde la puerta serial.

        @type maxChars: integer
        @param maxChars: maximo de caracteres ascii a leer
        @rtype: string
        @return: la linea de texto leida sin incluir el NL
        @raise TimeoutException: si no se pudieron leer la linea solicitada en el tiempo senalado
        """
        try:
            self.lock()
            linea = ''
            pos = 0
            tries = 0
            while( pos < maxChars + 1 and tries < self.maxTries ):
                b = self.serial.read(1)
                if( len( b )==0 ):
                    Utils.pause( 1 )
                    tries = tries + 1
                    continue
                if( type( b ) is str ):
                    if( b == '\n'):
                        return linea
                    linea = linea + b
                else:
                    if( b[0]==10 ):
                        return linea
                    linea =linea + chr(b[0])
                tries = 0
            raise self.TimeoutException
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def ignoreInput( self, timex ):
        """
        Descarta datos presentes para lectura en la puerta serial.

        @type timex: integer
        @param timex: tiempo en milisegundos que se leeran bytes los que seran descartados
        """
        try:
            self.lock()
            t = time.time()
            end = t + timex / 1000.0
            while( t < end ):
                try:
                    if( len( self.serial.read( 1 ) )==0 ):
                        Utils.pause( 1 )
                except:
                    pass
                t = time.time()
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def setDTR( self, value ):
        """Activa/desactiva la linea DTR."""
        self.serial.setDTR( value )
