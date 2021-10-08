# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para entregar informacion de la imagen capturada.

Es creada por la F2 y solo es util de lectura en la aplicacion

"""
class HF2Image:
    """Clase helper con la imagen capturada desde la F2."""

    def __init__( self, width, height, image ):
        """
        Inicializa los elemenos de lectura para la aplicacion.

        @type width: integer
        @param width: tamano de la imagen
        @type height: integer
        @param height: alto de la imagen
        @type image: bytearray
        @param image: la imagen capturada
        """
        self.width = width
        self.height = height
        self.image = image

    def __str__( self ):
        """Representacion modo texto de la clase."""
        return "F2Camera(%d, %d, %d)" % ( self.width, self.height, len( self.image ) )
