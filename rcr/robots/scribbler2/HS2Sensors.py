# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para entregar informacion del estado de varios sensores del S2.

Es creada por el S2 y solo es util de lectura en la aplicacion

"""
class HS2Sensors:
    """Clase helper con estado de varios sensores del S2."""

    def __init__( self, irLeft, irRight,
                        lightLeft, lightCenter, lightRight,
                        lineLeft, lineRight, stall ):
        """
        Inicializa los elementos de lectura para la aplicacion.

        @type irLeft: integer
        @param irLeft: valor del sensor IR iquierdo
        @type irRight: integer
        @param irRight: valor del sensor IR derecho
        @type lightLeft: integer
        @param lightLeft: valor del sensor de luz iquierdo
        @type lightCenter: integer
        @param lightCenter: valor del sensor de luz central
        @type lightRight: integer
        @param lightRight: valor del sensor de luz derecho
        @type lineLeft: integer
        @param lineLeft: valor del sensor de linea izquierdo
        @type lineRight: integer
        @param lineRight: valor del sensor de linea derecho
        @type stall: integer
        @param stall: valor indicador si las ruedas estan atrapadas
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
        """Representacion modo texto de la clase."""
        return "IR( %d, %d ), Light( %d, %d, %d ), Line( %d, %d ), Stall( %d )" % \
                (self.irLeft, self.irRight,
                 self.lightLeft, self.lightCenter, self.lightRight,
                 self.lineLeft, self.lineRight,
                 self.stall)
