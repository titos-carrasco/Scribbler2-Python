# -*- coding: utf-8 -*-

"""Acceso a puerta serial."""

import socket
import time

from .SerialInterface import SerialInterface
from . import Utils

class SerialNet( SerialInterface ):
    """Clase para interactuar con data serial via socket."""

    def __init__( self, host, port, timeout ):
        """
        Conecta al socket.

        @type host: string
        @param host: host a conectar
        @type port: integer
        @param port: puerta a conectar en el host
        @type timeout: integer
        @param timeout: timeout en milisegundos
        """
        super( SerialNet, self ).__init__()

        self.maxTries = timeout
        try:
            self.conn = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            self.conn.settimeout( 5.0 )
            self.conn.connect( ( host, port ) )
            self.conn.settimeout( 0 )
        except Exception as e:
            raise

    def close( self ):
        """Finaliza la conexion con el socket."""
        try:
            self.lock()
            self.conn.settimeout( self.maxTries )
            self.conn.close()
            self.conn = None
        except Exception as e:
            raise
        finally:
            self.unlock()

    def write( self, dataBytes ):
        """
        Envia bytes por el socket.

        @type dataBytes: byte, bytearray o equivalente
        @param dataBytes: bytes a enviar por la puerta serial
        """
        try:
            self.lock()
            self.conn.sendall( dataBytes )
        except Exception as e:
            raise
        finally:
            self.unlock()

    def read( self, nbytes ):
        """
        Lee bytes desde el socket.

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
                b = ''
                try:
                    b = self.conn.recv(1)
                except:
                    pass
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
        except Exception as e:
            raise
        finally:
            self.unlock()

    def readLine( self, maxChars ):
        """
        Lee una linea de texto finalizada en NL o del tamano especificado desde el socket.

        @type maxChars: integer
        @param maxChars: maximo de caracteres ascii a leer
        @rtype: string
        @return: la linea de texto leida sin incluir el NL
        @raise SerialTimeoutException: si no se pudieron leer la linea solicitada en el tiempo senalado
        """
        try:
            self.lock()
            linea = ''
            pos = 0
            tries = 0
            while( pos < maxChars + 1 and tries < self.maxTries ):
                b = ''
                try:
                    b = self.conn.recv(1)
                except:
                    pass
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
        except Exception as e:
            raise
        finally:
            self.unlock()

    def ignoreInput( self, timex ):
        """
        Descarta datos presentes para lectura en el socket.

        @type timex: integer
        @param timex: tiempo en milisegundos que se leeran bytes los que seran descartados
        """
        try:
            self.lock()
            t = time.time()
            end = t + timex / 1000.0
            while( t < end ):
                try:
                    if( len( self.conn.recv( 1 ) )==0 ):
                        Utils.pause( 1 )
                except:
                    pass
                t = time.time()
        except Exception as e:
            raise
        finally:
            self.unlock()
