# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para entregar informacion del estado de los motores del S2.

Es creada por el S2 y solo es util de lectura en la aplicacion

"""
class HS2MotorStats:
    """Clase helper con estado de los motores del S2."""

    def __init__( self, stat, moveReady ):
        """
        Inicializa los elementos de lectura para la aplicacion.

        @type stat: integer
        @param stat: estado de los motores (bitwise)
        @type moveReady: integer
        @param moveReady: indica si los motores estan listos
        """
        self.stat = stat
        self.moveReady = moveReady

    def __str__( self ):
        """Representacion modo texto de la clase."""
        return "HS2MotorStats(%d, %d)" % ( self.stat, self.moveReady )
