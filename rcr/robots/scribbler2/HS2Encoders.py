# -*- coding: utf-8 -*-

""" Clase de ayuda (helper) para entregar información de los encoders del S2

Es creada por el S2 y solo es útil de lectura en la aplicación

"""
class HS2Encoders:
    def __init__( self, left, right ):
        """ Inicializa los elementos de lectura para la aplicación

        Args:
            left (int): valor del encoder izquierdo
            right (int): valor del encoder derecho

        """
        self.left = left
        self.right = right

    def __str__( self ):
        return "HS2Encoders(%d, %d)" % ( self.left, self.right )
