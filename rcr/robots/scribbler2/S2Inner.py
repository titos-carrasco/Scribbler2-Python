# -*- coding: utf-8 -*-

""" Acceso al estado interno del S2

"""
from .HS2State import HS2State

class S2Inner:
    def __init__( self, s2 ):
        self.s2 = s2

    def getInfo( self ):
        """ Obtiene datos informativos del S2

        Returns:
            str: datos informativos del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 80 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getLineResponse( 128 )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getAllSensors( self ):
        """ Obtiene el estado de los principales sensores del S2

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 65 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getPass( self ):
        """ Obtiene la clave actualmente almacenada en el S2

        Returns:
            str: la clave actual almacenada
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 50 )
            self.s2.sendS2Command( packet, 0 )
            pass1 = self.s2.getBytesResponse( 8 )
            packet[0] = 51
            self.s2.sendS2Command( packet, 0 )
            pass2 = self.s2.getBytesResponse( 8 )
            return (pass1 + pass2).decode('ascii')
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getName( self ):
        """ Obtiene el nombre del S2

        Returns:
            str: el nombre del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 78 )
            self.s2.sendS2Command( packet, 0 )
            name1 = self.s2.getBytesResponse( 8 )
            packet[0] = 64
            self.s2.sendS2Command( packet, 0 )
            name2 = self.s2.getBytesResponse( 8 )
            return (name1 + name2).decode('ascii')
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getState( self ):
        """ Obtiene estado del S2

        Returns:
            HS2State: estado del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 77 )
            self.s2.sendS2Command( packet, 0 )
            return HS2State( self.s2.getUInt8Response(), self.s2.getUInt8Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getData( self ):
        """ Obtiene data almacenada en el S2

        Returns:
            bytearray[8]: data almacenada en el S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 81 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getBytesResponse( self.s2.DATA_LENGTH )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setPass( self, passw ):
        """ Establece la clave a almacenar en el S2

        Args:
            passwd (str[8]): clave a almacenar

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            bPass = passw.encode('ascii')
            packet = self.s2.makeS2Packet( 55 )
            i = 0
            while( i<len(bPass) and i<self.s2.DATA_LENGTH ):
                packet[i+1] = bPass[i]
                i = i + 1
            while( i<self.s2.DATA_LENGTH):
                packet[i+1] = 32
                i = i + 1
            self.s2.sendS2Command( packet, 0 )
            self.s2.getS2SensorsResponse()

            packet[0] = 56
            j = 0
            while( i<len(bPass) and j<self.s2.DATA_LENGTH ):
                packet[j+1] = bPass[i]
                i = i + 1
                j = j + 1
            while( j<self.s2.DATA_LENGTH ):
                packet[j+1] = 32
                j = j + 1
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setSingleData( self, pos, data):
        """ Almacena un dato en la zona de almacenamiento inerno del S2

        Args:
            pos (byte): posición en donde almacenar (0 a 7)
            data (byte): dato a almacenar (0 a 255)

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 96 )
            packet[1] = pos & 0x07
            packet[2] = data & 0xFF
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setData( self, data):
        """ Almacena un grupo de datos en la ona interna del S2

        Args:
            data (bytearray[8]): los datos a almacenar

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 97 )
            i = 0
            while( i<len(data) and  i<self.s2.DATA_LENGTH ):
                packet[i+1] = data[i]
                i = i + 1
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setName( self,  name ):
        """ Establece el nombre del S2

        Args:
            name (str): nombre a asignar (16 caracteres) al S2

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

        """
        try:
            self.s2.lock()
            bName = name.encode('ascii')
            packet = self.s2.makeS2Packet( 110 )
            i = 0
            while( i<len(bName) and i<self.s2.DATA_LENGTH ):
                packet[i+1] = bName[i]
                i = i + 1
            while( i<self.s2.DATA_LENGTH ):
                packet[i+1] = 32
                i = i + 1
            self.s2.sendS2Command( packet, 0 )
            self.s2.getS2SensorsResponse()

            packet[0] = 119
            j = 0
            while( i<len(bName) and j<self.s2.DATA_LENGTH ):
                packet[j+1] = bName[i]
                i = i + 1
                j = j + 1
            while( j<self.s2.DATA_LENGTH ):
                packet[j+1] = 32
                j = j + 1
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
