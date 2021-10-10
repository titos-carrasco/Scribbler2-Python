# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""

class HS2Infrared:
    """Valores de los sensores infrarojos del S2.

    ```
    irLeft :int - Valor del sensor infrarojo izquierdo
    irRight:int - Valor del sensor infrarojo derecho
    ```

    """

    def __init__(self, irLeft:int, irRight:int)->None:
        """Constructor."""
        self.irLeft = irLeft
        self.irRight = irRight

    def __str__(self):
        """Representacion modo texto de la clase."""
        return "HS2Infrared(%d, %d)" % (self.irLeft, self.irRight)
