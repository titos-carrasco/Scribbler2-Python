# -*- coding: utf-8 -*-

""" Clase de ayuda (helper) para entregar información del estado de los
motores del S2

Es creada por el S2 y solo es útil de lectura en la aplicación

"""
class HS2MotorStats:
    def __init__( self, stat, moveReady ):
        """ Inicializ alos elementos de lectura para la aplicación

        Args:
            stat (int): estado de los motores (bitwise)
            moveReady (int): indica si los motores están listos

        """
        self.stat = stat
        self.moveReady = moveReady

    def __str__( self ):
        return "HS2MotorStats(%d, %d)" % ( self.stat, self.moveReady )
