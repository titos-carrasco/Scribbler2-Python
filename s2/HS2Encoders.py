# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""

class HS2Encoders:
    """Valores de los encoders de las ruedas del S2.

    ```
    left :int - Valor del encoder de la rueda izquierda
    right:int - Valor del encoder de la rueda derecha
    ```
    """

    def __init__(self, left:int, right:int)->None:
        """Constructor."""
        self.left = left
        self.right = right

    def __str__(self):
        """Representacion modo texto de la clase."""
        return "HS2Encoders(%d, %d)" % (self.left, self.right)
