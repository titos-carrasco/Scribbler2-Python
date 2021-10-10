# -*- coding: utf-8 -*-

"""Interface para acceso a un dispositivo de manera serial."""

import threading

class ISerial():
    """Interface para interactuar de manera serial con un dispositivo."""

    class TimeoutException(Exception):
        """Timeout on data."""

    def close(self)->None:
        """Finaliza la conexion."""
        pass

    def write(self, dataBytes:bytes)->None:
        """Envia los 'dataBytes' al dispositivo."""
        pass

    def read(self, nbytes)->bytes:
        """Lee 'nbytes' bytes desde el dispositivo."""
        pass

    def readLine(self, maxChars:int)->str:
        """Lee una linea de texto finalizada en NL o hasta 'maxChars'."""
        pass

    def ignoreInput(self, timex:int):
        """Descarta durante 'timex' ms los datos presentes para lectura."""
        pass


    def readUInt8(self)->int:
        """Lee un entero, sin signo, de 8 bits."""
        b = self.read(1)
        return b[0] & 0xFF

    def readUInt16(self)->int:
        """Lee un entero, sin signo, de 16 bits."""
        b = self.read(2)
        n = b[0] & 0x000000FF
        n = (n<<8) | (b[1] & 0xFF)
        return n

    def readUInt32(self)->int:
        """Lee un entero sin signo de 32 bits."""
        b = self.read(4)
        n = b[0] & 0x000000FF
        n = (n << 8) | (b[1] & 0xFF)
        n = (n << 8) | (b[2] & 0xFF)
        n = (n << 8) | (b[3] & 0xFF)
        if((n & 0x80000000) != 0):
            return n - 0xFFFFFFFF -1
        else:
            return n

    def readInt32(self)->int:
        """Lee un entero, con signo, de 32 bits."""
        n = self.readUInt32()
        return int(n)

