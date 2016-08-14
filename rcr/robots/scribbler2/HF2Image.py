# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para entregar informacion de la imagen capturada.

Es creada por la F2 y solo es util de lectura en la aplicacion

"""
class HF2Image:
    """Clase helper con la imagen capturada desde la F2."""

    def __init__( self, width, height, image ):
        """Inicializa los elemenos de lectura para la aplicacion.

        Args:
            width (int): tamano de la imagen
            heignt (int): alto de la imagen
            image (bytearray): la imagen capturada

        """
        self.width = width
        self.height = height
        self.image = image

    def __str__( self ):
        """Representacion modo texto de la clase."""
        return "F2Camera(%d, %d, %d)" % ( self.width, self.height, len( self.image ) )
