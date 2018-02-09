# -*- coding: utf-8 -*-

"""Acceso a todas las funcionalidades del Scribbler2 (S2) y de la Fluke 2 (F2)."""

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
    """Clase central de interaccion con el S2."""

    DATA_LENGTH = 8
    PACKET_LENGTH = 9

    def __init__( self, port, speed, timeout ):
        """
        Corresponde al constructor de la clase.

        @type port: string
        @param port: la puerta a conectar con el S2
        @type speed: integer
        @param speed: velocidad de la conexion
        @type timeout: integer
        @param timeout: timeout para cada comando
        """
        self.mylock = threading.Lock()
        self.serial = Serial( port, speed, timeout )
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
        """Cierra la conexion al S2."""
        try:
            self.lock()
            self.serial.close()
        except Exception as e:
            raise
        finally:
            self.unlock()

    def getS2Inner( self ):
        """
        Obtiene acceso a los estados internos del S2.

        @rtype: L{S2Inner}
        @return: objeto con acceso a los datos internos del S2
        """
        return self.s2Inner

    def getS2IRSensors( self ):
        """
        Obtiene acceso a los sensores IR del S2.

        @rtype: L{S2IRSensors}
        @return: objeto con acceso a los sensores IR
        """
        return self.s2IRSensors

    def getS2LEDs( self ):
        """
        Obtiene acceso a los LEDs del S2.

        @rtype: L{S2LEDs}
        @return: objeto con acceso a los LEDs del S2
        """
        return self.s2LEDs

    def getS2LightSensors( self ):
        """
        Obtiene acceso a los sensores de luz del S2.

        @rtype: L{S2LightSensors}
        @return: objeto con acceso a los sensores de luz del S2
        """
        return self.s2LightSensors

    def getS2LineSensors( self ):
        """
        Obtiene acceso a los sensores de linea del S2.

        @rtype: L{S2LineSensors}
        @return: objeto con acceso a los sensores de linea del S2
        """
        return self.s2LineSensors

    def getS2Microphone( self ):
        """
        Obtiene acceso al microfono del S2.

        @rtype: L{S2Microphone}
        @return: objeto con acceso al micofono del del S2
        """
        return self.s2Microphone

    def getS2Motors( self ):
        """
        Obtiene acceso a los motores del S2.

        @rtype: L{S2Motors}
        @return: objeto con acceso a los motores del S2
        """
        return self.s2Motors

    def getS2Speaker( self ):
        """
        Obtiene acceso al parlante del S2.

        @rtype: L{S2Speaker}
        @return: objeto con acceso al parlante del S2
        """
        return self.s2Speaker

    def getS2Path( self ):
        """
        Obtiene acceso al modulo de trazado del S2.

        @rtype: L{S2Path}
        @return: objeto con acceso al modulo de trazado del S2
        """
        return self.s2Path

    def getF2Camera( self ):
        """
        Obtiene acceso a la camara del F2.

        @rtype: L{F2Camera}
        @return: objeto con acceso a la camara del F2
        """
        return self.f2Camera

    def getF2Inner( self ):
        """
        Obtiene acceso a los estados internos de la F2.

        @rtype: L{F2Inner}
        @return: objeto con acceso a los estados internos del F2
        """
        return self.f2Inner

    def getF2IRSensors( self ):
        """
        Obtiene acceso a los sensores IR de la F2.

        @rtype: L{F2IRSensors}
        @return: objeto con acceso a los sensores IR de la F2
        """
        return self.f2IRSensors

    def getF2LEDs( self ):
        """
        Obtiene acceso a los LEDs de la F2.

        @rtype: L{F2LEDs}
        @return: objeto con acceso a los LEDs de la F2
        """
        return self.f2LEDs

    def getF2Servos( self ):
        """
        Obtiene acceso al conector de servos de la F2.

        @rtype: L{F2Servos}
        @return: objeto con acceso al conector de servos de la F2
        """
        return self.f2Servos

    ## protected

    def makeS2Packet( self, cmd ):
        """
        Crea un paquete estandar utilizado como comando para el S2.

        @type cmd: byte
        @param cmd: comando a enviar
        @rtype: bytearray
        @return: paquete a completar con los parametros del comando (cmd)
        """
        packet = bytearray( self.PACKET_LENGTH )
        packet[0] = cmd & 0xFF
        return packet

    def sendS2Command( self, packet, pause ):
        """
        Envia un comando al S2.

        @type packet: bytearray
        @param packet: comando a enviar
        @type pause: integer
        @param pause: tiempo en ms a esperar por la respuesta luego de enviar el comando
        @rtype: bool
        @return: Verdadero si el ACK enviado por el S2 corresponde al esperado
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
        """
        Envia comando de trazado (path) al S2.

        @type packet: bytearray
        @param packet: comando de trazado a enviar
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
        """
        Envia comando a la tarjeta F2.

        @type packet: bytearray
        @param packet: comando a enviar a la F2
        @type pause: integer
        @param pause: pausa en ms a realizar una vez enviado el comando
        """
        self.serial.write( packet )
        if( pause > 0 ):
            Utils.pause( pause )

    def getS2SensorsResponse( self ):
        """
        Obtiene estado de los principales sensores del S2.

        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
        """
        return HS2Sensors( self.getUInt8Response() , self.getUInt8Response() ,
                           self.getUInt16Response(), self.getUInt16Response(), self.getUInt16Response(),
                           self.getUInt8Response() , self.getUInt8Response() ,
                           self.getUInt8Response() )

    def getLineResponse( self, maxChars ):
        """
        Obtiene una respuesta del S2 como un string ascii.

        @rtype: string
        @return: la respuesta del S2 como un string ascii
        """
        return self.serial.readLine( maxChars )

    def getUInt8Response( self ):
        """
        Obtiene una respuesta del S2 como un entero de 8 bits sin signo.

        @rtype: integer
        @return: la respuesta del S2 como uint8
        """
        return self.serial.readUInt8()

    def getUInt16Response( self ):
        """
        Obtiene una respuesta del S2 como un entero de 16 bits sin signo.

        @rtype: integer
        @return: la respuesta del S2 como uint16
        """
        return self.serial.readUInt16()

    def getUInt32Response( self ):
        """
        Obtiene una respuesta del S2 como un entero de 32 bits sin signo.

        @rtype: integer
        @return: la respuesta del S2 como uint32
        """
        return self.serial.readUInt32()

    def getInt32Response( self ):
        """
        Obtiene una respuesta del S2 como un entero de 32 bits con signo.

        @rtype: integer
        @return: la respuesta del S2 como int32
        """
        return self.serial.readInt32()

    def getBytesResponse( self, nbytes ):
        """
        Obtiene una respuesta del S2 como un conjunto de bytes.

        @type nbytes: integer
        @param nbytes: numero de bytes a leer
        @rtype: bytearray
        @return: la respuesta del S2
        """
        return self.serial.read( nbytes )

    def lock( self ):
        """Obtiene acceso exclusivo."""
        self.mylock.acquire()

    def unlock( self ):
        """Libera el acceso exclusivo."""
        self.mylock.release()
