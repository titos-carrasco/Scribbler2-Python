# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""

class HS2State:
    """Estado interno del S2.

    ```
    inPins :int - El valor de pines de entrada (bitwise)
    outPins:int - El valor de pines de salida (bitwise)
    ```
    """

    def __init__(self, inPins:int, outPins:int)->None:
        """Constructor."""
        self.inPins:int = inPins
        self.outPins:int = outPins

    def __str__(self):
        """Representacion modo texto de la clase."""
        return "HS2State(%d, %d)" % (self.inPins, self.outPins)
