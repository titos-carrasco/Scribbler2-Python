"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""


class HLights:
    """Valores de los sensores de luz del S2.

    ```
    light_left  :int - Valor del sensor de luz izquierdo
    light_center:int - Valor del sensor de luz central
    light_right :int - Valor del sensor de luz derecho
    ```
    """

    def __init__(self, light_left: int, light_center: int, light_right: int) -> None:
        """Constructor."""
        self.light_left = light_left
        self.light_center = light_center
        self.light_right = light_right

    def __str__(self):
        """Representacion modo texto de la clase."""
        return f"HLights({self.light_left}, {self.light_center}, {self.light_right}"
