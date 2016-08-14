# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para entregar informacion de coordenadas del S2.

Es creada por el S2 y solo es util de lectura en la aplicacion

"""
class HS2Coordinates:
    """Clase helper con datos de coordenadas del S2."""

    def __init__( self, x, y ):
        """Inicializa los elementos de lectura para la aplicacion.

        Args:
            x (int): coordenada x
            y (int): coordenada y
        """
        self.x = x
        self.y = y

    def __str__( self ):
        """Representacion modo texto de la clase."""
        return "HS2Coordinates(%d, %d)" % ( self.x, self.y )
