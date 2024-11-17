"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""


class HInfrared:
    """Valores de los sensores infrarojos del S2.

    ```
    ir_left :int - Valor del sensor infrarojo izquierdo
    ir_right:int - Valor del sensor infrarojo derecho
    ```

    """

    def __init__(self, ir_left: int, ir_right: int) -> None:
        """Constructor."""
        self.ir_left = ir_left
        self.ir_right = ir_right

    def __str__(self):
        """Representacion modo texto de la clase."""
        return f"HInfrared({self.ir_left}, {self.ir_right})"
