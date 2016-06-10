# -*- coding: utf-8 -*-

""" Clase de ayuda (helper) para entregar información de los sensores de línea
del S2

Es creada por el S2 y solo es útil de lectura en la aplicación

"""
class HS2LineSensors:
    def __init__( self, lineLeft, lineRight ):
        """ Inicializa los elementos de lectura para la aplicación

        Args:
            lineLeft (int): valor del sensor de línea izquierdo
            lineRight (int): valor del sensor de línea derecho

        """
        self.lineLeft = lineLeft
        self.lineRight = lineRight

    def __str__( self ):
        return "HS2LineSensors(%d, %d)" % ( self.lineLeft, self.lineRight )
