# -*- coding: utf-8 -*-

""" Clase de ayuda (helper) para entregar información de la imagen capturada

Es creada por la F2 y solo es útil de lectura en la aplicación

"""
class HF2Image:
    def __init__( self, width, height, image ):
        """ Inicializa los elemenos de lectura para la aplicación

        Args:
            width (int): tamaño de la imagen
            heignt (int): alto de la imagen
            image (bytearray): la imagen capturada

        """
        self.width = width
        self.height = height
        self.image = image

    def __str__( self ):
        return "F2Camera(%d, %d, %d)" % ( self.width, self.height, len( self.image ) )
