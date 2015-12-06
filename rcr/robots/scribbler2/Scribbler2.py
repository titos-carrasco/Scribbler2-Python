# -*- coding: utf-8 -*-

import threading
import time
import serial

from rcr.utils.Serial import Serial
from rcr.utils import Utils

from HS2Sensors import HS2Sensors

from S2Inner import S2Inner
from S2IRSensors import S2IRSensors
from S2LEDs import S2LEDs
from S2LightSensors import S2LightSensors
from S2LineSensors import S2LineSensors
from S2Microphone import S2Microphone
from S2Motors import S2Motors
from S2Speaker import S2Speaker
from S2Path import S2Path
from F2Camera import F2Camera
from F2Inner import F2Inner
from F2IRSensors import F2IRSensors
from F2LEDs import F2LEDs
from F2Servos import F2Servos

class Scribbler2:
    DATA_LENGTH = 8
    PACKET_LENGTH = 9

    def __init__( self, port, timeout ):
        self.mylock = threading.Lock()
        self.serial = Serial( port, 9600, timeout )
        Utils.pause( 1000 )
        self.serial.flushRead( 1000 )
        self.s2Inner = S2Inner( self )
        self.s2IRSensors = S2IRSensors( self )
        self.s2LEDs = S2LEDs( self )
        self.s2LightSensors = S2LightSensors( self )
        self.s2LineSensors = S2LineSensors( self )
        self.s2Microphone = S2Microphone( self )
        self.s2Motors = S2Motors( self )
        self.s2Speaker = S2Speaker( self )
        self.s2Path = S2Path( self )
        self.f2Camera = F2Camera( self )
        self.f2Inner = F2Inner( self )
        self.f2IRSensors = F2IRSensors( self )
        self.f2LEDs = F2LEDs( self )
        self.f2Servos = F2Servos( self )

    def close( self ):
        try:
            self.lock()
            self.serial.close()
        except Exception as e:
            raise
        finally:
            self.unlock()

    def getS2Inner( self ):
        return self.s2Inner

    def getS2IRSensors( self ):
        return self.s2IRSensors

    def getS2LEDs( self ):
        return self.s2LEDs

    def getS2LightSensors( self ):
        return self.s2LightSensors

    def getS2LineSensors( self ):
        return self.s2LineSensors

    def getS2Microphone( self ):
        return self.s2Microphone

    def getS2Motors( self ):
        return self.s2Motors

    def getS2Speaker( self ):
        return self.s2Speaker

    def getS2Path( self ):
        return self.s2Path

    def getF2Camera( self ):
        return self.f2Camera

    def getF2Inner( self ):
        return self.f2Inner

    def getF2IRSensors( self ):
        return self.f2IRSensors

    def getF2LEDs( self ):
        return self.f2LEDs

    def getF2Servos( self ):
        return self.f2Servos

    ## protected

    def makeS2Packet( self, cmd ):
        packet = bytearray( self.PACKET_LENGTH )
        packet[0] = cmd & 0xFF
        return packet

    def sendS2Command( self, packet, pause ):
        self.serial.write( packet )
        if( pause > 0 ):
            Utils.pause( pause )
        if( packet[0] != 0x50 ):
            b = self.serial.read( self.PACKET_LENGTH )
            if( packet != b ):
                Utils.debug( "Packet Mismatch:" )
                Utils.debug( packet )
                Utils.debug( b )
                return False
        return True

    def sendS2PathCommand( self, packet ):
        self.serial.write( packet )
        t = time.time()
        while( time.time() - t  < 3.5 ):
            try:
                b = self.serial.read( self.PACKET_LENGTH )
                if( packet != b ):
                    Utils.debug( "Packet Mismatch (path):" )
                    Utils.debug( packet )
                    Utils.debug( b )
                    raise serial.SerialTimeoutException
                return
            except serial.SerialTimeoutException as e:
                pass

        # necesitamos sincronizar las respuestas, lo hacemos con GetAll()
        packet = self.makeS2Packet( 65 )
        while( True ):
            self.serial.write( packet )
            try:
                self.serial.read( 11 ) # estos bytes quedaron sin ser recibidos
                self.serial.read( self.PACKET_LENGTH )
                break
            except serial.SerialTimeoutException as e:
                pass

        # solicitamos el estado de los sensores
        self.sendS2Command( packet, 0 )

    def sendF2Command( self, packet, pause ):
        self.serial.write( packet )
        if( pause > 0 ):
            Utils.pause( pause )

    def getS2SensorsResponse( self ):
        return HS2Sensors( self.getUInt8Response() , self.getUInt8Response() ,
                           self.getUInt16Response(), self.getUInt16Response(), self.getUInt16Response(),
                           self.getUInt8Response() , self.getUInt8Response() ,
                           self.getUInt8Response() )

    def getLineResponse( self, maxChars ):
        return self.serial.readLine( maxChars )

    def getUInt8Response( self ):
        return self.serial.readUInt8()

    def getUInt16Response( self ):
        return self.serial.readUInt16()

    def getUInt32Response( self ):
        return self.serial.readUInt32()

    def getInt32Response( self ):
        return self.serial.readInt32()

    def getBytesResponse( self, nbytes ):
        return self.serial.read( nbytes )

    def lock( self ):
        """Obtiene acceso exclusivo."""
        self.mylock.acquire()

    def unlock( self ):
        """Libera el acceso exclusivo."""
        self.mylock.release()
