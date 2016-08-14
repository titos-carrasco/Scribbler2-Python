# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para entregar informacion de los sensores de luz del S2.

Es creada por el S2 y solo es util de lectura en la aplicacion

"""
class HS2Lights:
    """Clase helper con datos de los sensores de luz del S2."""

    def __init__( self, lightLeft, lightCenter , lightRight ):
        """Inicializa los elementos de lectura para la aplicacion.

        Args:
            lightLeft (int): valor del sensor de luz izquierdo
            lightCenter (int): valor del sensor de luz central
            lightRight (int): valor del sensor de luz derecho

        """
        self.lightLeft = lightLeft
        self.lightCenter = lightCenter
        self.lightRight = lightRight

    def __str__( self ):
        """Representacion modo texto de la clase."""
        return "HS2Lights(%d, %d, %d)" % ( self.lightLeft, self.lightCenter, self.lightRight )
