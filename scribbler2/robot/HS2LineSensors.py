# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""

class HS2LineSensors:
    """Valores de los sensores de linea del S2.

    ```
    lineLeft :int - Valor del sensor de linea izquierdo
    lineRight:int - Valor del sensor de linea derecho
    ```
    """

    def __init__(self, lineLeft:int, lineRight:int)->None:
        """Constructor."""
        self.lineLeft = lineLeft
        self.lineRight = lineRight

    def __str__(self):
        """Representacion modo texto de la clase."""
        return "HS2LineSensors(%d, %d)" % (self.lineLeft, self.lineRight)
