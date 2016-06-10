# -*- coding: utf-8 -*-

""" Clase de ayuda (helper) para entregar información de coordenadas del S2

Es creada por el S2 y solo es útil de lectura en la aplicación

"""
class HS2Coordinates:
    def __init__( self, x, y ):
        """ Inicializa los elementos de lectura para la aplicación

        Args:
            x (int): coordenada x
            y (int): coordenada y
        """
        self.x = x
        self.y = y

    def __str__( self ):
        return "HS2Coordinates(%d, %d)" % ( self.x, self.y )
