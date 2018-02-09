# -*- coding: utf-8 -*-

"""Acceso al estado interno del S2."""

from .HS2State import HS2State

class S2Inner:
    """Clase de acceso al estado interno del S2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def getInfo( self ):
        """
        Obtiene datos informativos del S2.

        @rtype: string
        @return: datos informativos del S2
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
        """
        Obtiene el estado de los principales sensores del S2.

        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Obtiene la clave actualmente almacenada en el S2.

        @rtype: string
        @return: la clave actual almacenada
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
        """
        Obtiene el nombre del S2.

        @rtype: string
        @return: el nombre del S2
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
        """
        Obtiene estado del S2.

        @rtype: L{HS2State}
        @return: estado del S2
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
        """
        Obtiene data almacenada en el S2.

        @rtype: bytearray[8]
        @return: data almacenada en el S2
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
        """
        Establece la clave a almacenar en el S2.

        @type passw: string[8]
        @param passw: clave a almacenar
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Almacena un dato en la zona de almacenamiento inerno del S2.

        @type pos: byte
        @param pos: posicion en donde almacenar (0 a 7)
        @type data: byte
        @param data: dato a almacenar (0 a 255)
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Almacena un grupo de datos en la ona interna del S2.

        @type data: btearray[8]
        @param data: los datos a almacenar
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
        """
        Establece el nombre del S2.

        @type name: sytring
        @param name: nombre a asignar (16 caracteres) al S2
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
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
