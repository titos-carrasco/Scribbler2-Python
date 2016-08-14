# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para entregar informacion de los sensores de linea del S2.

Es creada por el S2 y solo es util de lectura en la aplicacion

"""
class HS2LineSensors:
    """Clase helper con datos de los sensores de linea del S2."""

    def __init__( self, lineLeft, lineRight ):
        """Inicializa los elementos de lectura para la aplicacion.

        Args:
            lineLeft (int): valor del sensor de linea izquierdo
            lineRight (int): valor del sensor de linea derecho

        """
        self.lineLeft = lineLeft
        self.lineRight = lineRight

    def __str__( self ):
        """Representacion modo texto de la clase."""
        return "HS2LineSensors(%d, %d)" % ( self.lineLeft, self.lineRight )
