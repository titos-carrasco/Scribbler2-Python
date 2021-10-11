# -*- coding: utf-8 -*-

"""Acceso a todas las funcionalidades del Scribbler2 y de la Fluke2 via BT."""

import time

from scribbler2.robot.Scribbler2 import Scribbler2
from scribbler2.Serial import Serial
from scribbler2.HF2Image import HF2Image

class S2Fluke2(Scribbler2):
    """Clase para interactuar con un Scribbler2 que posee una Fluke2."""

    FLUKE_FORWARD       = 1
    SCRIBBLER_FORWARD   = 2
    IMAGE_LARGE         = 1
    IMAGE_SMALL         = 2
    IMAGE_GRAYJPEG      = 1
    IMAGE_GRAYJPEG_FAST = 2
    IMAGE_JPEG          = 3
    IMAGE_JPEG_FAST     = 4


    def __init__(self, port:str="", bauds:int=115200, timeout:int=500)->None:
        """Inicializa el objeto y lo conecta a la Fluke2."""
        self.image_width  = 0
        self.image_height = 0

        conn = Serial(port, bauds, timeout)
        time.sleep(2.0)

        super(S2Fluke2, self).__init__(conn)

    def setPicSize(self, size:int):
        """Establece tamano de la imagen a capturar desde la F2.

        'size' puede ser:
        - Fluke2.IMAGE_LARGE: 1280x800
        - Fluke2.IMAGE_SMALL: 427x266
        """
        try:
            self._lock()
            if(size == self.IMAGE_LARGE):
                s = 213
                w = 1280
                h = 800
            else: # if(size == self.IMAGE_SMALL)
                s = 71
                w = 427
                h = 266
            packet = bytearray(2)
            packet[0] = 11
            packet[1] = s
            self._sendF2Command(packet, 0.1)
            self.image_width = w
            self.image_height = h
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getImage(self, formato:int)->bytearray:
        """Captura imagen desde la F2 en el formato especificado.

        El 'formato' de la imagen puede ser:
        - Fluke2.IMAGE_GRAYJPEG      : tonos de gris
        - Fluke2.IMAGE_GRAYJPEG_FAST : tonos de gris
        - Fluke2.IMAGE_JPEG          : color
        - Fluke2.IMAGE_JPEG_FAST     : color
        """
        try:
            self._lock()
            if(formato == self.IMAGE_GRAYJPEG):
                reg = 1
                cmd_header = 135
                cmd = 136
            elif(formato == self.IMAGE_GRAYJPEG_FAST):
                reg = 0
                cmd_header = 135
                cmd = 136
            elif(formato == self.IMAGE_JPEG):
                reg = 1
                cmd_header = 137
                cmd = 138
            else: # if(formato == self.IMAGE_JPEG_FAST)
                reg = 0
                cmd_header = 137
                cmd = 138
            packet = bytearray(1)
            packet[0] = cmd_header
            self._sendF2Command(packet, 0.1)

            header_len = self._getUInt8Response() + (self._getUInt8Response() << 8)
            image = self._getBytesResponse(header_len)
            image = bytearray( image )

            packet = bytearray(2)
            packet[0] = cmd
            packet[1] = reg
            self._sendF2Command(packet, 0.1)

            last = 0x00
            while(True):
                b = self._getUInt8Response()
                image.append(b)
                if(b == 0xD9 and last == 0xFF):
                    self._getUInt32Response()
                    self._getUInt32Response()
                    self._getUInt32Response()
                    break
                last = b
            return HF2Image(self.image_width, self.image_height, image)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def whiteBalanceOn(self)->None:
        """Activa balance de blancos."""
        try:
            self._lock()
            packet = bytearray(1)
            packet[0] = 129
            self._sendF2Command(packet, 0.1)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def whiteBalanceOff(self)->None:
        """Desactiva balance de blancos."""
        try:
            self._lock()
            packet = bytearray(1)
            packet[0] = 130
            self._sendF2Command(packet, 0.1)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setCameraParam(self, addr:int, value:int)->None:
        """Establece parametros especificos para la camara del F2."""
        try:
            self._lock()
            packet = bytearray(3)
            packet[0] = 131
            packet[1] = addr & 0xFF
            packet[2] = value & 0xFF
            self._sendF2Command(packet, 0.1)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setWindow(self, window:int, xLow:int, yLow:int,
                        xHigh:int, yHigh:int, xStep:int, yStep:int)->None:
        """Establece parametros de la ventana de captura."""
        try:
            self._lock()
            packet = bytearray(12)
            packet[0] = 127
            packet[1] = window & 0xFF
            packet[2] = (xLow >> 8) & 0xFF
            packet[3] = xLow & 0xFF
            packet[4] = (yLow >> 8) & 0xFF
            packet[5] = yLow & 0xFF
            packet[6] = (xHigh >> 8) & 0xFF
            packet[7] = xHigh & 0xFF
            packet[8] = (yHigh >> 8) & 0xFF
            packet[9] = yHigh & 0xFF
            packet[10] = xStep & 0xFF
            packet[11] = yStep & 0xFF
            self._sendF2Command(packet, 0.1)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getVersion(self)->str:
        """Obtiene version de la F2."""
        try:
            self._lock()
            packet = bytearray(1)
            packet[0] = 142
            self._sendF2Command(packet, 0.1)
            return self._getLineResponse(128)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def identifyRobot(self)->str:
        """Obtiene infromacion que identifica al S2/F2."""
        try:
            self._lock()
            packet = bytearray(1)
            packet[0] = 156
            self._sendF2Command(packet, 0.1)
            id = self._getLineResponse(128)
            time.sleep(4.0)
            return id
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getBattery(self)->float:
        """Obtiene voltaje de la bateria."""
        try:
            self._lock()
            packet = bytearray(1)
            packet[0] = 89
            self._sendF2Command(packet, 0.1)
            return self._getUInt16Response() / 20.9813
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setForwardness(self, forwardness:int)->None:
        """Establece cual es el frente del S2/F2 para ciertos comandos.

        'forwardness' (orientación del S2/F2) puede ser:
        - Fluke2.FLUKE_FORWARD    : la tarjeta F2 es el frente
        - Fluke2.SCRIBBLER_FORWARD: los sensores de luz son el frente
        """
        try:
            self._lock()
            if(forwardness == self.FLUKE_FORWARD):
                f = 1
            else: # if(forwardness == self.SCRIBBLER_FORWARD)
                f = 0
            packet = bytearray(2)
            packet[0] = 128
            packet[1] = f
            self._sendF2Command(packet, 0.1)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getErrors(self)->str:
        """Obtiene el log de errores almacenados en la F2."""
        try:
            self._lock()
            packet = bytearray(1)
            packet[0] = 10
            self._sendF2Command(packet, 0.1)
            n = self._getUInt16Response()
            log = self._getBytesResponse(n)
            return log.decode('ascii')
        except Exception as e:
            raise
        finally:
            self._unlock()

    def resetScribbler(self)->None:
        """Resetea el S2/F2."""
        try:
            self._lock()
            packet = bytearray(1)
            packet[0] = 124
            self._sendF2Command(packet, 0.1)
            time.sleep(4.0)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setIRPower(self, pwm:int):
        """Establece el valor de energia (0-255) para el sensor IR."""
        try:
            self._lock()
            packet = bytearray(2)
            packet[0] = 120
            packet[1] = pwm & 0xFF
            self._sendF2Command(packet, 0.1)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getIR(self)->int:
        """Obtiene valor del sensor IR de la F2."""
        try:
            self._lock()
            packet = bytearray(1)
            packet[0] = 86
            self._sendF2Command(packet, 0.1)
            return self._getUInt16Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setBrightLed(self, pwm:int)->None:
        """Establece potencia (0 a 255) del Led de la F2."""
        try:
            self._lock()
            packet = bytearray(2)
            packet[0] = 126
            packet[1] = pwm & 0xFF
            self._sendF2Command(packet, 0.1)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setServo(self, idservo:int, value:int)->None:
        """Establece el valor (0 a 255) del servo (0 a 3) conectado a la F2."""
        try:
            self._lock()
            packet = bytearray(3)
            packet[0] = 12
            packet[1] = idservo & 0x03
            packet[2] = value & 0xFF
            self._sendF2Command(packet, 0.1)
        except Exception as e:
            raise
        finally:
            self._unlock()

    ## protected

    def _sendF2Command(self, packet:bytearray, pause:int=0)->None:
        """Envia comando a la tarjeta F2 espeficando una pausa."""
        self.conn.write(packet)
        if(pause > 0):
            time.sleep(pause)
