# -*- coding: utf-8 -*-

import serial
import threading
import time
import Utils

class Serial:
    def __init__( self, port, bauds, timeout ):
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
        try:
            self.lock()
            self.serial.close()
            self.serial = None
        except Exception as e:
            raise
        finally:
            self.unlock()

    def write( self, bytes ):
        try:
            self.lock()
            self.serial.write( bytes )
            self.serial.flush()
        except Exception as e:
            raise
        finally:
            self.unlock()

    def read( self, nbytes ):
        try:
            self.lock()
            bytes = bytearray( nbytes )
            pos = 0
            tries = 0
            while( pos < nbytes and tries < self.maxTries ):
                b = self.serial.read(1)
                if( b == '' ):
                    Utils.pause(1)
                    tries = tries + 1
                    continue
                bytes[ pos ] = b
                pos = pos + 1
                tries = 0
            if( pos < nbytes ):
                raise serial.SerialTimeoutException
            return bytes
        except Exception as e:
            raise
        finally:
            self.unlock()

    def readLine( self, maxChars ):
        try:
            self.lock()
            bytes = ''
            pos = 0
            tries = 0
            while( pos < maxChars + 1 and tries < self.maxTries ):
                b = self.serial.read(1)
                if( b == '' ):
                    Utils.pause(1)
                    tries = tries + 1
                    continue
                if( b == "\n" ):
                    return bytes
                bytes = bytes + b
                tries = 0
            raise serial.SerialTimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def flushRead( self, timex ):
        try:
            self.lock()
            t = time.time()
            end = t + timex / 1000.0
            while( t < timex ):
                try:
                    if(self.serial.read(1)==''):
                        Utils.pause(1);
                except:
                    pass
                t = time.time()
        except Exception as e:
            raise
        finally:
            self.unlock()

    def readUInt8( self ):
        b = self.read(1)
        return b[0] & 0xFF

    def readUInt16( self ):
        b = self.read(2)
        n = b[0] & 0x000000FF
        n = ( n<<8 ) | ( b[1] & 0xFF )
        return n

    def readUInt32( self ):
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
        n = self.readUInt32()
        return int( n )

    #### Privadas

    def lock( self ):
        """Obtiene acceso exclusivo."""
        self.mylock.acquire()

    def unlock( self ):
        """Libera el acceso exclusivo."""
        self.mylock.release()
