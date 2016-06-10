# -*- coding: utf-8 -*-

""" Acceso a todas las funcionalidades del Scribbler2 (S2) y de la Fluke 2 (F2)

"""

import threading
import time
import serial

from rcr.utils.Serial import Serial
from rcr.utils import Utils

from .HS2Sensors import HS2Sensors

from .S2Inner import S2Inner
from .S2IRSensors import S2IRSensors
from .S2LEDs import S2LEDs
from .S2LightSensors import S2LightSensors
from .S2LineSensors import S2LineSensors
from .S2Microphone import S2Microphone
from .S2Motors import S2Motors
from .S2Speaker import S2Speaker
from .S2Path import S2Path
from .F2Camera import F2Camera
from .F2Inner import F2Inner
from .F2IRSensors import F2IRSensors
from .F2LEDs import F2LEDs
from .F2Servos import F2Servos

class Scribbler2:
    DATA_LENGTH = 8
    PACKET_LENGTH = 9

    def __init__( self, port, timeout ):
        """ Inicia la conexión

        Args:
            port (str): la puerta a conectar
            timeout (int): timeout para cada comando

        """
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
        """ Cierra la conexión al S2

        """
        try:
            self.lock()
            self.serial.close()
        except Exception as e:
            raise
        finally:
            self.unlock()

    def getS2Inner( self ):
        """ Obtiene acceso a los estados internos del S2

        Returns:
            S2Inner: objeto con acceso a los datos internos del S2
        """
        return self.s2Inner

    def getS2IRSensors( self ):
        """ Obtiene acceso a los sensores IR del S2

        Returns;
            S2IRSensor: objeto con acceso a los sensores IR

        """
        return self.s2IRSensors

    def getS2LEDs( self ):
        """ Obtiene acceso a los LEDs del S2

        Returns:
            S2LEDs: objeto con acceso a los LEDs del S2

        """
        return self.s2LEDs

    def getS2LightSensors( self ):
        """ Obtiene acceso a los sensores de luz del S2

        Returns:
            S2LightsSensors: objeto con acceso a los sensores de luz del S2

        """
        return self.s2LightSensors

    def getS2LineSensors( self ):
        """ Obtiene acceso a los sensores de línea del S2

        Returns:
            S2LightsSensors: objeto con acceso a los sensores de línea del S2

        """
        return self.s2LineSensors

    def getS2Microphone( self ):
        """ Obtiene acceso al micrófono del S2

        Returns:
            S2Microphone: objeto con acceso al micófono del del S2

        """
        return self.s2Microphone

    def getS2Motors( self ):
        """ Obtiene acceso a los motores del S2

        Returns:
            S2Motors: objeto con acceso a los motores del S2

        """
        return self.s2Motors

    def getS2Speaker( self ):
        """ Obtiene acceso al parlante del S2

        Returns:
            S2Speaker: objeto con acceso al parlante del S2

        """
        return self.s2Speaker

    def getS2Path( self ):
        """ Obtiene acceso al módulo de trazado del S2

        Returns:
            S2Path: objeto con acceso al módulo de trazado del S2

        """
        return self.s2Path

    def getF2Camera( self ):
        """ Obtiene acceso a la cámara del F2

        Returns:
            F2Camera: objeto con acceso a la cámara del F2

        """
        return self.f2Camera

    def getF2Inner( self ):
        """ Obtiene acceso a los estados internos de la F2

        Returns:
            F2Inner: objeto con acceso a los estados internos del F2

        """
        return self.f2Inner

    def getF2IRSensors( self ):
        """ Obtiene acceso a los sensores IR de la F2

        Returns:
            F2Inner: objeto con acceso a los sensores IR de la F2

        """
        return self.f2IRSensors

    def getF2LEDs( self ):
        """ Obtiene acceso a los LEDs de la F2

        Returns:
            F2Inner: objeto con acceso a los LEDs de la F2

        """
        return self.f2LEDs

    def getF2Servos( self ):
        """ Obtiene acceso al conector de servos de la F2

        Returns:
            F2Servos: objeto con acceso al conector de servos de la F2

        """
        return self.f2Servos

    ## protected

    def makeS2Packet( self, cmd ):
        """ Crea un paquete estándar utilizado como comando para el S2

        Args:
            cmd (byte): comando a enviar

        Returns;
            bytearray: paquete a completar con los parámetros del comando (cmd)

        """
        packet = bytearray( self.PACKET_LENGTH )
        packet[0] = cmd & 0xFF
        return packet

    def sendS2Command( self, packet, pause ):
        """ Envía un comando al S2

        Args:
            packet (bytearray): comando a enviar
            pause (int): tiempo en ms a esperar luego de enviar el comando

        Return:
            bool: Verdadero si el ACK enviado por el S2 no corresponde

        """
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
        """ Envía comando de trazado (path) al S2

        Args:
            packet (bytearray): comando de trazado a enviar

        """
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
        """ Envía comando a la tarjeta F2

        Args:
            packet (bytearray): comando a enviar a la F2
            pause (int): pausa en ms a realizar una vez enviado el comando

        """
        self.serial.write( packet )
        if( pause > 0 ):
            Utils.pause( pause )

    def getS2SensorsResponse( self ):
        """ Obtiene estado de los principales sensores del S2

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        return HS2Sensors( self.getUInt8Response() , self.getUInt8Response() ,
                           self.getUInt16Response(), self.getUInt16Response(), self.getUInt16Response(),
                           self.getUInt8Response() , self.getUInt8Response() ,
                           self.getUInt8Response() )

    def getLineResponse( self, maxChars ):
        """ Obtiene una respuesta del S2 como un string ascii

        Returns:
            str: la respuesta del S2 como un string ascii
        """
        return self.serial.readLine( maxChars )

    def getUInt8Response( self ):
        """ Obtiene una respuesta del S2 como un entero de 8 bits sin signo

        Returns:
            int: la respuesta del S2 como uint8
        """
        return self.serial.readUInt8()

    def getUInt16Response( self ):
        """ Obtiene una respuesta del S2 como un entero de 16 bits sin signo

        Returns:
            int: la respuesta del S2 como uint16
        """
        return self.serial.readUInt16()

    def getUInt32Response( self ):
        """ Obtiene una respuesta del S2 como un entero de 32 bits sin signo

        Returns:
            int: la respuesta del S2 como uint32
        """
        return self.serial.readUInt32()

    def getInt32Response( self ):
        """ Obtiene una respuesta del S2 como un entero de 32 bits con signo

        Returns:
            int: la respuesta del S2 como int32
        """
        return self.serial.readInt32()

    def getBytesResponse( self, nbytes ):
        """ Obtiene una respuesta del S2 como un conjunto de bytes

        Args:
            nbytes (int): bytes a leer

        Returns:
            bytearray: la respuesta del S2

        """
        return self.serial.read( nbytes )

    def lock( self ):
        """ Obtiene acceso exclusivo

        """
        self.mylock.acquire()

    def unlock( self ):
        """ Libera el acceso exclusivo

        """
        self.mylock.release()
