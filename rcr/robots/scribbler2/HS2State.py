# -*- coding: utf-8 -*-

""" Clase de ayuda (helper) para entregar información del estado del S2

Es creada por el S2 y solo es útil de lectura en la aplicación

"""
class HS2State:
    def __init__( self, inPins, outPins ):
        """ Inicializa los elementos de lectura para la aplicación

        Args:
            inPins (int): valor de pines de entrada (bitwise)
            outPins (int): valor de pines de salida (bitwise)

        """
        self.inPins = inPins
        self.outPins = outPins

    def __str__( self ):
        return "HS2State(%d, %d)" % ( self.inPins, self.outPins )
