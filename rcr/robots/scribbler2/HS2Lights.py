# -*- coding: utf-8 -*-

""" Clase de ayuda (helper) para entregar información de los sensores de luz
 del S2

Es creada por el S2 y solo es útil de lectura en la aplicación

"""
class HS2Lights:
    def __init__( self, lightLeft, lightCenter , lightRight ):
        """ Inicializa los elementos de lectura para la aplicación

        Args:
            lightLeft (int): valor del sensor de luz izquierdo
            lightCenter (int): valor del sensor de luz central
            lightRight (int): valor del sensor de luz derecho

        """
        self.lightLeft = lightLeft
        self.lightCenter = lightCenter
        self.lightRight = lightRight

    def __str__( self ):
        return "HS2Lights(%d, %d, %d)" % ( self.lightLeft, self.lightCenter, self.lightRight )
