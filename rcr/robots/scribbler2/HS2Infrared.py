# -*- coding: utf-8 -*-

""" Clase de ayuda (helper) para entregar información de los sensores
infrarojos del S2

Es creada por el S2 y solo es útil de lectura en la aplicación

"""
class HS2Infrared:
    def __init__( self, irLeft, irRight ):
        """ Inicializa los elementos de lectura para la aplicación

        Args:
            irLeft (int): valor del sensor infrarojo izquierdo
            irRight (int): valor del sensor infrarojo derecho

        """
        self.irLeft = irLeft
        self.irRight = irRight

    def __str__( self ):
        return "HS2Infrared(%d, %d)" % (self.irLeft, self.irRight)
