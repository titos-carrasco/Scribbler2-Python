# -*- coding: utf-8 -*-

""" Clase de ayuda (helper) para entregar información del estado de varios
sensores del S2

Es creada por el S2 y solo es útil de lectura en la aplicación

"""
class HS2Sensors:
    def __init__( self, irLeft, irRight,
                        lightLeft, lightCenter, lightRight,
                        lineLeft, lineRight, stall ):
        """ Inicializa los elementos de lectura para la aplicación

        Args;
            irLeft (int); valor del sensor IR iquierdo
            irRight (int): valor del sensor IR derecho
            lightLeft (nt): valor del sensor de luz iquierdo
            lightCenter (int): valor del sensor de luz central
            lightRight (int): valor del sensor de luz derecho
            lineLeft (int): valor del sensor de línea izquierdo
            lineRight (int): valor del sensor de línea derecho
            stall (int): valor indicador si las ruedas están atrapadas

        """
        self.irLeft = irLeft
        self.irRight = irRight
        self.lightLeft = lightLeft
        self.lightCenter = lightCenter
        self.lightRight = lightRight
        self.lineLeft = lineLeft
        self.lineRight = lineRight
        self.stall = stall

    def __str__( self ):
        return "IR( %d, %d ), Light( %d, %d, %d ), Line( %d, %d ), Stall( %d )" % \
                (self.irLeft, self.irRight,
                 self.lightLeft, self.lightCenter, self.lightRight,
                 self.lineLeft, self.lineRight,
                 self.stall)
