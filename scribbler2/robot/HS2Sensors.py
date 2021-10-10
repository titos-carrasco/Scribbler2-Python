# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""

class HS2Sensors:
    """Valor de varios sensores del S2.

    ```
    irLeft     :int - Valor del sensor IR izquierdo
    irRight    :int - Valor del sensor IR derecho
    lightLeft  :int - Valor del sensor de luz izquierdo
    lightCenter:int - Valor del sensor de luz central
    lightRight :int - Valor del sensor de luz derecho
    lineLeft   :int - Valor del sensor de linea izquierdo
    lineRight  :int - Valor del sensor de linea derecho
    stall      :int - Indicador de que lso motores estan trabados
    ```
    """

    def __init__(self, irLeft:int, irRight:int,
                       lightLeft:int, lightCenter:int, lightRight:int,
                       lineLeft:int, lineRight:int, stall:int)->None:
        """Constructor."""
        self.irLeft = irLeft
        self.irRight = irRight
        self.lightLeft = lightLeft
        self.lightCenter = lightCenter
        self.lightRight = lightRight
        self.lineLeft = lineLeft
        self.lineRight = lineRight
        self.stall = stall

    def __str__(self):
        """Representacion modo texto de la clase."""
        return "IR(%d, %d), Light(%d, %d, %d), Line(%d, %d), Stall(%d)" % \
                (self.irLeft, self.irRight,
                 self.lightLeft, self.lightCenter, self.lightRight,
                 self.lineLeft, self.lineRight,
                 self.stall)
