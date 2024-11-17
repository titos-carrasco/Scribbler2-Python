"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""


class HSensors:
    """Valor de varios sensores del S2.

    ```
    ir_left     :int - Valor del sensor IR izquierdo
    ir_right    :int - Valor del sensor IR derecho
    light_left  :int - Valor del sensor de luz izquierdo
    light_center:int - Valor del sensor de luz central
    light_right :int - Valor del sensor de luz derecho
    line_left   :int - Valor del sensor de linea izquierdo
    line_right  :int - Valor del sensor de linea derecho
    stall      :int - Indicador de que lso motores estan trabados
    ```
    """

    def __init__(
        self,
        ir_left: int,
        ir_right: int,
        light_left: int,
        light_center: int,
        light_right: int,
        line_left: int,
        line_right: int,
        stall: int,
    ) -> None:
        """Constructor."""
        self.ir_left = ir_left
        self.ir_right = ir_right
        self.light_left = light_left
        self.light_center = light_center
        self.light_right = light_right
        self.line_left = line_left
        self.line_right = line_right
        self.stall = stall

    def __str__(self):
        """Representacion modo texto de la clase."""
        return f"IR({self.ir_left}, {self.ir_right}), \
                 Light({self.light_left}, {self.light_center}, {self.light_right}), \
                 Line({self.line_left}, {self.line_right}), \
                 Stall({self.stall})"
