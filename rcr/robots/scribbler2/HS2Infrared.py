# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para entregar informacion de los sensores infrarojos del S2.

Es creada por el S2 y solo es util de lectura en la aplicacion

"""
class HS2Infrared:
    """Clase helper con datos de los sensores infrarojos del S2."""

    def __init__( self, irLeft, irRight ):
        """Inicializa los elementos de lectura para la aplicacion.

        Args:
            irLeft (int): valor del sensor infrarojo izquierdo
            irRight (int): valor del sensor infrarojo derecho

        """
        self.irLeft = irLeft
        self.irRight = irRight

    def __str__( self ):
        """Representacion modo texto de la clase."""
        return "HS2Infrared(%d, %d)" % (self.irLeft, self.irRight)
