# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""

class HS2MotorStats:
    """Estado de los motores del S2.

    ```
    stat     :int - Estado de los motores (bitwise)
    moveReady:int - Indicador de que los motores estan listos
    ```
    """

    def __init__(self, stat:int, moveReady:int)->None:
        """Constructor."""
        self.stat = stat
        self.moveReady = moveReady

    def __str__(self):
        """Representacion modo texto de la clase."""
        return "HS2MotorStats(%d, %d)" % (self.stat, self.moveReady)
