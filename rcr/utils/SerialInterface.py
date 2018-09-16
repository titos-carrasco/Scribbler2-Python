# -*- coding: utf-8 -*-

"""Acceso a data serial."""

import threading

class SerialInterface( object ):
    """Clase para interactuar con data serial."""

    class TimeoutException( Exception ):
        """Timeout on data."""


    def __init__( self  ):
        """Inicializa la conexión."""
        self.mylock = threading.Lock()

    def close( self ):
        """Finaliza la conexion."""
        pass

    def write( self, dataBytes ):
        """Envia bytes."""
        pass

    def read( self, nbytes ):
        """Lee bytes."""
        pass

    def readLine( self, maxChars ):
        """Lee una linea de texto finalizada en NL o del tamano especificado."""
        pass

    def ignoreInput( self, timex ):
        """Descarta durante un tiempo los datos presentes para lectura."""
        pass

    def readUInt8( self ):
        """
        Lee un entero sin signo de 8 bits.

        @rtype: integer
        @return: el entero sin signo de 8 bits
        """
        b = self.read(1)
        return b[0] & 0xFF

    def readUInt16( self ):
        """
        Lee un entero sin signo de 16 bits.

        @rtype: integer
        @return: el entero sin signo de 16 bits
        """
        b = self.read(2)
        n = b[0] & 0x000000FF
        n = ( n<<8 ) | ( b[1] & 0xFF )
        return n

    def readUInt32( self ):
        """
        Lee un entero sin signo de 32 bits.

        @rtype: integer
        @return: el entero sin signo de 32 bits
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
        """
        Lee un entero con signo de 32 bits.

        @rtype: integer
        @return: el entero con signo de 32 bits
        """
        n = self.readUInt32()
        return int( n )

    #### Privadas

    def lock( self ):
        """Obtiene acceso exclusivo a una zona."""
        self.mylock.acquire()

    def unlock( self ):
        """Libera el acceso exclusivo a una zona."""
        self.mylock.release()
