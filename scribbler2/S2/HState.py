# -*- coding: utf-8 -*-

"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""


class HState:
    """Estado interno del S2.

    ```
    in_pins :int - El valor de pines de entrada (bitwise)
    out_pins:int - El valor de pines de salida (bitwise)
    ```
    """

    def __init__(self, in_pins: int, out_pins: int) -> None:
        """Constructor."""
        self.in_pins: int = in_pins
        self.out_pins: int = out_pins

    def __str__(self):
        """Representacion modo texto de la clase."""
        return f"HS2State({self.in_pins}, {self.out_pins})"
