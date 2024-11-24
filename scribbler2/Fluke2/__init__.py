"""Acceso a todas las funcionalidades del Scribbler2 y de la Fluke2 via BT.

la Fluke2 tieme un timeout interno de 300ms para que los comandos redireccionados
al S2 envien su respuesta
"""

import time
import scribbler2.S2
from scribbler2.Fluke2.HImage import HImage


class Robot(scribbler2.S2.Robot):
    """Clase para interactuar con un Scribbler2 que posee una Fluke2."""

    FLUKE_FORWARD = 1
    SCRIBBLER_FORWARD = 2
    IMAGE_LARGE = 1
    IMAGE_SMALL = 2
    IMAGE_GRAYJPEG = 1
    IMAGE_GRAYJPEG_FAST = 2
    IMAGE_JPEG = 3
    IMAGE_JPEG_FAST = 4

    def __init__(self, port: str, timeout: float = 1.0, delay: float = 0.0) -> None:
        """Inicializa el objeto y lo conecta a la Fluke2."""
        super().__init__(port, baudrate=115200, timeout=timeout, delay=delay)
        self.image_width = 0
        self.image_height = 0

    def setPicSize(self, size: int):
        """Establece tamano de la imagen a capturar desde la F2.

        'size' puede ser:
        - Fluke2.IMAGE_LARGE: 1280x800
        - Fluke2.IMAGE_SMALL: 427x266
        """
        if size == self.IMAGE_LARGE:
            s = 213
            w = 1280
            h = 800
        else:  # if(size == self.IMAGE_SMALL)
            s = 71
            w = 427
            h = 266
        packet = bytearray(2)
        packet[0] = 11
        packet[1] = s
        self._sendF2Command(packet)
        self.image_width = w
        self.image_height = h

    def getImage(self, formato: int) -> bytearray:
        """Captura imagen desde la F2 en el formato especificado.

        El 'formato' de la imagen puede ser:
        - Fluke2.IMAGE_GRAYJPEG      : tonos de gris
        - Fluke2.IMAGE_GRAYJPEG_FAST : tonos de gris
        - Fluke2.IMAGE_JPEG          : color
        - Fluke2.IMAGE_JPEG_FAST     : color
        """
        if formato == self.IMAGE_GRAYJPEG:
            reg = 1
            cmd_header = 135
            cmd = 136
        elif formato == self.IMAGE_GRAYJPEG_FAST:
            reg = 0
            cmd_header = 135
            cmd = 136
        elif formato == self.IMAGE_JPEG:
            reg = 1
            cmd_header = 137
            cmd = 138
        else:  # if(formato == self.IMAGE_JPEG_FAST)
            reg = 0
            cmd_header = 137
            cmd = 138
        packet = bytearray(1)
        packet[0] = cmd_header
        self._sendF2Command(packet)

        header_len = self._getUInt8Response() + (self._getUInt8Response() << 8)
        image = self._getBytesResponse(header_len)
        image = bytearray(image)

        packet = bytearray(2)
        packet[0] = cmd
        packet[1] = reg
        self._sendF2Command(packet)

        last = 0x00
        while True:
            b = self._getUInt8Response()
            image.append(b)
            if b == 0xD9 and last == 0xFF:
                self._getUInt32Response()
                self._getUInt32Response()
                self._getUInt32Response()
                break
            last = b
        return HImage(self.image_width, self.image_height, image)

    def whiteBalanceOn(self) -> None:
        """Activa balance de blancos."""
        packet = bytearray(1)
        packet[0] = 129
        self._sendF2Command(packet)

    def whiteBalanceOff(self) -> None:
        """Desactiva balance de blancos."""
        packet = bytearray(1)
        packet[0] = 130
        self._sendF2Command(packet)

    def setCameraParam(self, addr: int, value: int) -> None:
        """Establece parametros especificos para la camara del F2."""
        packet = bytearray(3)
        packet[0] = 131
        packet[1] = addr & 0xFF
        packet[2] = value & 0xFF
        self._sendF2Command(packet)

    def setWindow(
        self,
        window: int,
        x_low: int,
        y_low: int,
        x_high: int,
        y_high: int,
        x_step: int,
        y_step: int,
    ) -> None:
        """Establece parametros de la ventana de captura."""
        packet = bytearray(12)
        packet[0] = 127
        packet[1] = window & 0xFF
        packet[2] = (x_low >> 8) & 0xFF
        packet[3] = x_low & 0xFF
        packet[4] = (y_low >> 8) & 0xFF
        packet[5] = y_low & 0xFF
        packet[6] = (x_high >> 8) & 0xFF
        packet[7] = x_high & 0xFF
        packet[8] = (y_high >> 8) & 0xFF
        packet[9] = y_high & 0xFF
        packet[10] = x_step & 0xFF
        packet[11] = y_step & 0xFF
        self._sendF2Command(packet)

    def getVersion(self) -> str:
        """Obtiene version de la F2."""
        packet = bytearray(1)
        packet[0] = 142
        self._sendF2Command(packet)
        return self._getLineResponse(128)

    def identifyRobot(self) -> str:
        """Obtiene infromacion que identifica al S2/F2."""
        packet = bytearray(1)
        packet[0] = 156
        self._sendF2Command(packet)
        id_robot = self._getLineResponse(128)
        time.sleep(4.0)
        return id_robot

    def getBattery(self) -> float:
        """Obtiene voltaje de la bateria."""
        packet = bytearray(1)
        packet[0] = 89
        self._sendF2Command(packet)
        return self._getUInt16Response() / 20.9813

    def setForwardness(self, forwardness: int) -> None:
        """Establece cual es el frente del S2/F2 para ciertos comandos.

        'forwardness' (orientación del S2/F2) puede ser:
        - Fluke2.FLUKE_FORWARD    : la tarjeta F2 es el frente
        - Fluke2.SCRIBBLER_FORWARD: los sensores de luz son el frente
        """
        if forwardness == self.FLUKE_FORWARD:
            f = 1
        else:  # if(forwardness == self.SCRIBBLER_FORWARD)
            f = 0
        packet = bytearray(2)
        packet[0] = 128
        packet[1] = f
        self._sendF2Command(packet)

    def getErrors(self) -> str:
        """Obtiene el log de errores almacenados en la F2."""
        packet = bytearray(1)
        packet[0] = 10
        self._sendF2Command(packet)
        n = self._getUInt16Response()
        log = self._getBytesResponse(n)
        return log.decode("ascii")

    def reset(self, delay: float = 3.0) -> None:
        """Resetea el S2/F2."""
        packet = bytearray(1)
        packet[0] = 124
        self._sendF2Command(packet)
        time.sleep(delay)
        self.flushBuffers()

    def setIRPower(self, pwm: int):
        """Establece el valor de energia (0-255) para el sensor IR."""
        packet = bytearray(2)
        packet[0] = 120
        packet[1] = pwm & 0xFF
        self._sendF2Command(packet)

    def getIR(self) -> int:
        """Obtiene valor del sensor IR de la F2."""
        packet = bytearray(1)
        packet[0] = 86
        self._sendF2Command(packet)
        return self._getUInt16Response()

    def setBrightLed(self, pwm: int) -> None:
        """Establece potencia (0 a 255) del Led de la F2."""
        packet = bytearray(2)
        packet[0] = 126
        packet[1] = pwm & 0xFF
        self._sendF2Command(packet)

    def setServo(self, idservo: int, value: int) -> None:
        """Establece el valor (0 a 255) del servo (0 a 3) conectado a la F2."""
        packet = bytearray(3)
        packet[0] = 12
        packet[1] = idservo & 0x03
        packet[2] = value & 0xFF
        self._sendF2Command(packet)

    ## protected

    def _sendF2Command(self, packet: bytearray, pause: int = 100) -> None:
        """Envia comando a la tarjeta F2 especificando una pausa en ms."""
        self.conn.write(packet)
        if pause > 0:
            time.sleep(pause / 1000.0)
