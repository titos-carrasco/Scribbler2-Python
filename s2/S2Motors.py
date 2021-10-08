# -*- coding: utf-8 -*-

"""Acceso a los motores del S2."""

from s2.HS2MotorStats import HS2MotorStats
from s2.HS2Encoders import HS2Encoders

class S2Motors:
    """Clase de acceso a los motores del S2."""

    def __init__( self, s2 ):
        """
        Corresponde al constructor de la clase.

        @type s2: L{Scribbler2}
        @param s2: referencia al S2 que lo contiene
        """
        self.s2 = s2

    def getMotorStats( self ):
        """
        Obtiene el estado de los motores del S2.

        @rtype: L{HS2MotorStats}
        @return: estado de los motores del S2
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 170 )
            self.s2.sendS2Command( packet, 0 )
            return HS2MotorStats( self.s2.getUInt32Response(), self.s2.getUInt8Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getEncoders( self, preserve ):
        """
        Obtiene estado de los encoders del S2.

        @type preserve: byte
        @param preserve: conserva (1) o borra (0) el valor de los encoder al leer
        @rtype: L{HS2Encoders}
        @return: estado de los encoders
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 171 )
            packet[1] = preserve & 0x01
            self.s2.sendS2Command( packet, 0 )
            return HS2Encoders( self.s2.getUInt32Response(), self.s2.getUInt32Response() )
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def getStall( self ):
        """
        Obtiene estado de las ruedas (atrapadas).

        @rtype: integer
        @return: indicador si las ruedas estan atrapadas
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 79 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getUInt8Response()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setMotorsOff( self ):
        """
        Apaga los motores del S2.

        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
        """
        try:
            self.s2.lock()
            packet = self.s2.makeS2Packet( 108 )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()

    def setMotors( self, left, right):
        """
        Enciende los motores del S2.

        @type left: integer
        @param left: porcentaje de potencia al motor izquierdo (-100 a 100)
        @type right: integer
        @param right: porcentaje de potencia al motor derecho (-100 a 100)
        @rtype: L{HS2Sensors}
        @return: objeto con el valor de los principales sensores del S2
        """
        try:
            self.s2.lock()
            if(left>100):
                left = 100
            elif(left<-100):
                left = -100
            left = left + 100

            if(right>100):
                right = 100
            elif(right<-100):
                right = -100
            right = right + 100

            packet = self.s2.makeS2Packet( 109 )
            packet[1] = int( right )
            packet[2] = int( left )
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
