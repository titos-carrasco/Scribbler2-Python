# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""

class HS2Lights:
    """Valores de los sensores de luz del S2.

    ```
    lightLeft  :int - Valor del sensor de luz izquierdo
    lightCenter:int - Valor del sensor de luz central
    lightRight :int - Valor del sensor de luz derecho
    ```
    """

    def __init__(self, lightLeft:int, lightCenter:int, lightRight:int)->None:
        """Constructor."""
        self.lightLeft = lightLeft
        self.lightCenter = lightCenter
        self.lightRight = lightRight

    def __str__(self):
        """Representacion modo texto de la clase."""
        return "HS2Lights(%d, %d, %d)" % (self.lightLeft, self.lightCenter, self.lightRight)
