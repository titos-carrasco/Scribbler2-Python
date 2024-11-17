"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Scribbler2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""


class HMotorStats:
    """Estado de los motores del S2.

    ```
    stat     :int - Estado de los motores (bitwise)
    move_ready:int - Indicador de que los motores estan listos
    ```
    """

    def __init__(self, stat: int, move_ready: int) -> None:
        """Constructor."""
        self.stat = stat
        self.move_ready = move_ready

    def __str__(self):
        """Representacion modo texto de la clase."""
        return f"HMotorStats({self.stat}, {self.move_ready})"
