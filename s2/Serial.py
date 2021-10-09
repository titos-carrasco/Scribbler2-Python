# -*- coding: utf-8 -*-

"""Acceso a puerta serial.

Es utilizada exclusivamente por la clase **Scribbler2**.
"""

import serial
import time

from s2.SerialInterface import SerialInterface

class Serial(SerialInterface):
    """Clase para interactuar con puerta serial."""

    def __init__(self, port:str, bauds:int, timeout:int)->None:
        """Conecta a la puerta serial especificada por 'port'.

        Si se especifica, la conexión se realiza a los 'bauds' indicados
        y/o con un 'timeout' dado en milisegundos
        """
        super(Serial, self).__init__()

        self.maxTries = timeout
        try:
            self.serial = serial.Serial(port, baudrate=bauds, bytesize=8,
                                       parity='N', stopbits=1,
                                       timeout=0)
            self.serial.flushInput()
            self.serial.flushOutput()
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise

    def close(self)->None:
        """Finaliza la conexion con la puerta serial."""
        try:
            self.lock()
            self.serial.close()
            self.serial = None
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def write(self, dataBytes:bytes)->None:
        """Envia 'dataBytes' por la puerta serial."""
        try:
            self.lock()
            self.serial.write(dataBytes)
            self.serial.flush()
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def read(self, nbytes)->bytes:
        """Lee 'nbytes' desde la puerta serial."""
        try:
            self.lock()
            dataBytes = bytearray(nbytes)
            pos = 0
            tries = 0
            while(pos < nbytes and tries < self.maxTries):
                b = self.serial.read(1)
                if(len(b)==0):
                    time.sleep(0.001)
                    tries = tries + 1
                    continue
                if(type(b) is str):
                    dataBytes[pos] = ord(b)
                else:
                    dataBytes[pos] = b[0]
                pos = pos + 1
                tries = 0
            if(pos < nbytes):
                raise self.TimeoutException
            return dataBytes
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def readLine(self, maxChars)->str:
        """Lee una linea de texto finalizada en NL.

        'maxChars' especifica el máximo número de caracteres a leer.
        El caracter NL no es incluido en la linea retornada
        """
        try:
            self.lock()
            linea = ''
            pos = 0
            tries = 0
            while(pos < maxChars + 1 and tries < self.maxTries):
                b = self.serial.read(1)
                if(len(b)==0):
                    time.sleep(0.001)
                    tries = tries + 1
                    continue
                if(type(b) is str):
                    if(b == '\n'):
                        return linea
                    linea = linea + b
                else:
                    if(b[0]==10):
                        return linea
                    linea =linea + chr(b[0])
                tries = 0
            raise self.TimeoutException
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def ignoreInput(self, timex:int)->None:
        """Descarta durante 'timex' ms los datos presentes para lectura."""
        try:
            self.lock()
            t = time.time()
            end = t + timex / 1000.0
            while(t < end):
                try:
                    if(len(self.serial.read(1))==0):
                        time.sleep(0.001)
                except:
                    pass
                t = time.time()
        except serial.SerialTimeoutException:
            raise self.TimeoutException
        except Exception as e:
            raise
        finally:
            self.unlock()

    def setDTR(self, value:bool)->None:
        """Activa/desactiva la linea DTR."""
        self.serial.setDTR(value)
