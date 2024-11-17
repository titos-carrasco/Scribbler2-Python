"""Clase de ayuda (helper) para retornar informacion del S2.

Es creada exclusivamente por metodos de la clase **Fluke2** y retornadas
a su invocador. Sus atributos pueden ser accesados directamente.
"""


class HImage:
    """Imagen capturada desde la F2.

    ```
    - width :int       - ancho de la imagen
    - height:int       - alto de la imagen
    - image :bytearray - bytes que componen la imagen
    ```
    """

    def __init__(self, width: int, height: int, image: bytearray) -> None:
        """Constructor."""
        self.width = width
        self.height = height
        self.image = image

    def __str__(self):
        """Representacion modo texto de la clase."""
        return f"HImage({self.width}, {self.height}, {len(self.image)})"
