# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para entregar informacion de los encoders del S2.

Es creada por el S2 y solo es util de lectura en la aplicacion

"""
class HS2Encoders:
    """Clase helper con datos de los encoders del S2."""

    def __init__( self, left, right ):
        """
        Inicializa los elementos de lectura para la aplicacion.

        @type left: integer
        @param left: valor del encoder izquierdo
        @type right: integer
        @param right: valor del encoder derecho
        """
        self.left = left
        self.right = right

    def __str__( self ):
        """Representacion modo texto de la clase."""
        return "HS2Encoders(%d, %d)" % ( self.left, self.right )
