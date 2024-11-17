"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""


class HLineSensors:
    """Valores de los sensores de linea del S2.

    ```
    line_left :int - Valor del sensor de linea izquierdo
    line_right:int - Valor del sensor de linea derecho
    ```
    """

    def __init__(self, line_left: int, line_right: int) -> None:
        """Constructor."""
        self.line_left = line_left
        self.line_right = line_right

    def __str__(self):
        """Representacion modo texto de la clase."""
        return f"HLineSensors({self.line_left}, {self.line_right})"
