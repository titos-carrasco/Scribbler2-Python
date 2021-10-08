# -*- coding: utf-8 -*-

"""Acceso a todas las funcionalidades del Scribbler2 (S2)."""

import threading
import time

from s2.Serial import Serial
from s2.HS2Sensors import HS2Sensors
from s2.S2Inner import S2Inner
from s2.S2IRSensors import S2IRSensors
from s2.S2LEDs import S2LEDs
from s2.S2LightSensors import S2LightSensors
from s2.S2LineSensors import S2LineSensors
from s2.S2Microphone import S2Microphone
from s2.S2Motors import S2Motors
from s2.S2Speaker import S2Speaker
from s2.S2Path import S2Path

class Scribbler2( object ):
    """Clase central de interaccion con el S2."""

    DATA_LENGTH = 8
    PACKET_LENGTH = 9

    def __init__( self, port=None, bauds=38400, timeout=500, dtr=None ):
        """
        Corresponde al constructor de la clase.

        type port: string
        param port: la puerta a conectar con el S2
        type bauds: integer
        param bauds: velocidad de la conexion
        type timeout: integer
        param timeout: timeout para cada comando
        """
        self.mylock = threading.Lock()
        self.s2Inner = S2Inner( self )
        self.s2IRSensors = S2IRSensors( self )
        self.s2LEDs = S2LEDs( self )
        self.s2LightSensors = S2LightSensors( self )
        self.s2LineSensors = S2LineSensors( self )
        self.s2Microphone = S2Microphone( self )
        self.s2Motors = S2Motors( self )
        self.s2Speaker = S2Speaker( self )
        self.s2Path = S2Path( self )

        self.conn = Serial( port, bauds, timeout )
        if( not dtr is None ):
            self.conn.setDTR( dtr )
        time.sleep( 2.0 )
        self.conn.ignoreInput( 1000 )

    def close( self ):
        """Cierra la conexion al S2."""
        try:
            self.lock()
            self.conn.close()
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
        self.conn.write( packet )
        if( pause > 0 ):
            time.sleep( pause )
        if( packet[0] != 0x50 ):
            b = self.conn.read( self.PACKET_LENGTH )
            if( packet != b ):
                print( "Packet Mismatch:" )
                return False
        return True

    def sendS2PathCommand( self, packet ):
        """
        Envia comando de trazado (path) al S2.

        @type packet: bytearray
        @param packet: comando de trazado a enviar
        """
        self.conn.write( packet )
        t = time.time()
        while( time.time() - t  < 3.5 ):
            try:
                b = self.conn.read( self.PACKET_LENGTH )
                if( packet != b ):
                    print( "Packet Mismatch (path):" )
                    raise self.conn.TimeoutException
                return
            except self.conn.TimeoutException as e:
                pass

        # necesitamos sincronizar las respuestas, lo hacemos con GetAll()
        packet = self.makeS2Packet( 65 )
        while( True ):
            self.conn.write( packet )
            try:
                self.conn.read( 11 ) # estos bytes quedaron sin ser recibidos
                self.conn.read( self.PACKET_LENGTH )
                break
            except self.conn.TimeoutException as e:
                pass

        # solicitamos el estado de los sensores
        self.sendS2Command( packet, 0 )


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
        return self.conn.readLine( maxChars )

    def getUInt8Response( self ):
        """
        Obtiene una respuesta del S2 como un entero de 8 bits sin signo.

        @rtype: integer
        @return: la respuesta del S2 como uint8
        """
        return self.conn.readUInt8()

    def getUInt16Response( self ):
        """
        Obtiene una respuesta del S2 como un entero de 16 bits sin signo.

        @rtype: integer
        @return: la respuesta del S2 como uint16
        """
        return self.conn.readUInt16()

    def getUInt32Response( self ):
        """
        Obtiene una respuesta del S2 como un entero de 32 bits sin signo.

        @rtype: integer
        @return: la respuesta del S2 como uint32
        """
        return self.conn.readUInt32()

    def getInt32Response( self ):
        """
        Obtiene una respuesta del S2 como un entero de 32 bits con signo.

        @rtype: integer
        @return: la respuesta del S2 como int32
        """
        return self.conn.readInt32()

    def getBytesResponse( self, nbytes ):
        """
        Obtiene una respuesta del S2 como un conjunto de bytes.

        @type nbytes: integer
        @param nbytes: numero de bytes a leer
        @rtype: bytearray
        @return: la respuesta del S2
        """
        return self.conn.read( nbytes )

    def lock( self ):
        """Obtiene acceso exclusivo."""
        self.mylock.acquire()

    def unlock( self ):
        """Libera el acceso exclusivo."""
        self.mylock.release()
