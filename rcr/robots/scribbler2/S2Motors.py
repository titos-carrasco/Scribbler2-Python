# -*- coding: utf-8 -*-

""" Acceso a los motores del S2

"""
from .HS2MotorStats import HS2MotorStats
from .HS2Encoders import HS2Encoders

class S2Motors:
    def __init__( self, s2 ):
        self.s2 = s2

    def getMotorStats( self ):
        """ Obtiene el estado de los motores del S2

        Returns:
            HS2MotorStats: estado de los motores del S2

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
        """ Obtiene estado de los encoders del S2

        Args:
            preserve (byte): conserva (1) o borra (0) el valor de los encoder al leer

        Returns:
            HS2Encoders: estado de los encoders

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
        """ Obtiene estado de las ruedas (atrapadas)

        Returns:
            int: indicador si las ruedas están atrapadas

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
        """ Apaga los motores del S2

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

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
        """ Enciende los motores del S2

        Args:
            left (int): porcentaje de potencia al motor izquierdo (-100 a 100)
            right (int): porcentaje de potencia al motor derecho (-100 a 100)

        Returns:
            HS2Sensors: objeto con el valor de los principales sensores del S2

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
            packet[1] = right
            packet[2] = left
            self.s2.sendS2Command( packet, 0 )
            return self.s2.getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self.s2.unlock()
