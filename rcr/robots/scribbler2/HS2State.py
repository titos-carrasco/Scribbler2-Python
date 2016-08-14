# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para entregar informacion del estado del S2.

Es creada por el S2 y solo es util de lectura en la aplicacion

"""
class HS2State:
    """Clase helper para el S2 con estado interno."""

    def __init__( self, inPins, outPins ):
        """Inicializa los elementos de lectura para la aplicacion.

        Args:
            inPins (int): valor de pines de entrada (bitwise)
            outPins (int): valor de pines de salida (bitwise)

        """
        self.inPins = inPins
        self.outPins = outPins

    def __str__( self ):
        """Representacion modo texto de la clase."""
        return "HS2State(%d, %d)" % ( self.inPins, self.outPins )
