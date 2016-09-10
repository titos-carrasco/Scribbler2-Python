# -*- coding: utf-8 -*-

"""Acceso a puerta serial."""

import serial
import threading
import time
from . import Utils

class Serial:
    """Clase para interactuar con puerta serial."""

    def __init__( self, port, bauds, timeout ):
        """Conecta a la puerta serial.

        Args:
            port (str): puerta serial
            baudrate (int): velocidad
            bytesize(opcional[int]): numero de bits (8)
            parity (opcional[char]): paridad ('N')
            stopbits (opcional[int]): numero de bits de parada (1)
            timeout(opcional[int]): timeout en milisegundos (0)

        """
        self.maxTries = timeout
        self.mylock = threading.Lock()
        try:
            self.serial = serial.Serial(port, baudrate=bauds, bytesize=8,
                                       parity='N', stopbits=1,
                                       timeout=0 )
            self.serial.flushInput()
            self.serial.flushOutput()
        except Exception as e:
            raise

    def close( self ):
        """Finaliza la conexion con la puerta serial."""
        try:
            self.lock()
            self.serial.close()
            self.serial = None
        except Exception as e:
            raise
        finally:
            self.unlock()

    def write( self, dataBytes ):
        """Envia bytes por la puerta serial.

        Args:
            dataBytes (bytes, bytearray o compatibles): bytes a enviar

        """
        try:
            self.lock()
            self.serial.write( dataBytes )
            self.serial.flush()
        except Exception as e:
            raise
        finally:
            self.unlock()

    def read( self, nbytes ):
        """Lee bytes desde la puerta serial.

        Args:
            nbytes (int): numero de bytes a leer

        Returns:
            bytearray: los bytes leidos

        Raises:
            SerialTimeoutException: si no se pudieron leer los bytes solicitados en el tiempo senalado

        """
        try:
            self.lock()
            dataBytes = bytearray( nbytes )
            pos = 0
            tries = 0
            while( pos < nbytes and tries < self.maxTries ):
                b = self.serial.read(1)
                if( len(b)==0 ):
                    Utils.pause(1)
                    tries = tries + 1
                    continue
                if( type(b) is str ):
                    dataBytes[pos] = ord(b)
                else:
                    dataBytes[pos] = b[0]
                pos = pos + 1
                tries = 0
            if( pos < nbytes ):
                raise serial.SerialTimeoutException
            return dataBytes
        except Exception as e:
            raise
        finally:
            self.unlock()

    def readLine( self, maxChars ):
        """Lee una linea ascii finalizada en NL o de tamano especifico desde la puerta serial.

        Args:
            maxChars (int): maximo de caracteres ascii a leer

        Raises:
            SerialTimeoutException: si no se pudieron leer la linea solicitada en el tiempo senalado

        Returns:
            str: la linea de texto leida sin incluir el NL

        """
        try:
            self.lock()
            linea = ''
            pos = 0
            tries = 0
            while( pos < maxChars + 1 and tries < self.maxTries ):
                b = self.serial.read(1)
                if( len(b)==0 ):
                    Utils.pause(1)
                    tries = tries + 1
                    continue
                if( type(b) is str ):
                    if( b == '\n'):
                        return linea
                    linea = linea + b
                else:
                    if( b[0]==10 ):
                        return linea
                    linea =linea + chr(b[0])
                tries = 0
            raise serial.SerialTimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def flushRead( self, timex ):
        """Descarta datos presentes para lectura en la puerta serial.

        Args:
            timex (int): tiempo en milisegundos que se leeran bytes y seran descartados

        """
        try:
            self.lock()
            t = time.time()
            end = t + timex / 1000.0
            while( t < end ):
                try:
                    if( len(self.serial.read(1))==0 ):
                        Utils.pause(1);
                except:
                    pass
                t = time.time()
        except Exception as e:
            raise
        finally:
            self.unlock()

    def readUInt8( self ):
        """Lee un entero sin signo de 8 bits.

        Returns:
            int: el entero sin signo de 8 bits

        """
        b = self.read(1)
        return b[0] & 0xFF

    def readUInt16( self ):
        """Lee un entero sin signo de 16 bits.

        Returns:
            int: el entero sin signo de 16 bits

        """
        b = self.read(2)
        n = b[0] & 0x000000FF
        n = ( n<<8 ) | ( b[1] & 0xFF )
        return n

    def readUInt32( self ):
        """Lee un entero sin signo de 32 bits.

        Returns:
            int: el entero sin signo de 32 bits

        """
        b = self.read(4)
        n = b[0] & 0x000000FF
        n = ( n << 8 ) | ( b[1] & 0xFF )
        n = ( n << 8 ) | ( b[2] & 0xFF )
        n = ( n << 8 ) | ( b[3] & 0xFF )
        if( ( n & 0x80000000 ) != 0 ):
            return n - 0xFFFFFFFF -1
        else:
            return n

    def readInt32(self):
        """Lee un entero con signo de 32 bits.

        Returns:
            int: el entero con signo de 32 bits

        """
        n = self.readUInt32()
        return int( n )

    #### Privadas

    def lock( self ):
        """Obtiene acceso exclusivo."""
        self.mylock.acquire()

    def unlock( self ):
        """Libera el acceso exclusivo."""
        self.mylock.release()
