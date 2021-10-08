# -*- coding: utf-8 -*-

"""Acceso a todas las funcionalidades del Scribbler2 (S2) y de la Fluke 2 (F2)."""

import time

from s2.Scribbler2 import Scribbler2
from s2.F2Camera import F2Camera
from s2.F2Inner import F2Inner
from s2.F2IRSensors import F2IRSensors
from s2.F2LEDs import F2LEDs
from s2.F2Servos import F2Servos

class Fluke2( Scribbler2 ):
    """Clase central de interaccion con la F2."""

    def __init__( self, port="", bauds=9600, timeout=500 ):
        """
        Corresponde al constructor de la clase.

        @type port: string
        @param port: la puerta a conectar con la F2
        @type bauds: integer
        @param bauds: velocidad de la conexion
        @type timeout: integer
        @param timeout: timeout para cada comando
        """
        self.f2Camera = F2Camera( self )
        self.f2Inner = F2Inner( self )
        self.f2IRSensors = F2IRSensors( self )
        self.f2LEDs = F2LEDs( self )
        self.f2Servos = F2Servos( self )

        super( Fluke2, self ).__init__( port=port, bauds=bauds, timeout=timeout )

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

    def sendF2Command( self, packet, pause ):
        """
        Envia comando a la tarjeta F2.

        @type packet: bytearray
        @param packet: comando a enviar a la F2
        @type pause: integer
        @param pause: pausa en ms a realizar una vez enviado el comando
        """
        self.conn.write( packet )
        if( pause > 0 ):
            time.sleep( pause )
