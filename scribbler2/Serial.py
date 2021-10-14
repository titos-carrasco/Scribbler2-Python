# -*- coding: utf-8 -*-

"""Acceso a puerta serial."""

import serial
import time

from scribbler2.robot.ISerial import ISerial

class Serial(ISerial):
    """Clase para interactuar con puerta serial."""

    def __init__(self, port:str, bauds:int, timeout:int)->None:
        """Conecta a la puerta serial especificada por 'port'.

        Si se especifica, la conexión se realiza a los 'bauds' indicados
        y/o con un 'timeout' dado en milisegundos
        """
        super(Serial, self).__init__()

        self.serial = serial.Serial(port, baudrate=bauds, bytesize=8,
                                   parity='N', stopbits=1,
                                   timeout=timeout/1000.0)
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()

    def close(self)->None:
        """Finaliza la conexion con la puerta serial."""
        try:
            self.serial.close()
        except:
            pass
        self.serial = None

    def write(self, dataBytes:bytes)->None:
        """Envia 'dataBytes' por la puerta serial."""
        self.serial.write(dataBytes)
        self.serial.flush()

    def available(self)->int:
        """El numero de bytes disponibles para lectura."""
        return self.serial.in_waiting

    def read(self, nbytes)->bytes:
        """Lee 'nbytes' desde la puerta serial."""
        dataBytes = bytearray(nbytes)
        pos = 0
        while(pos < nbytes):
            b = self.serial.read(1)
            if( len(b) == 0 ):
                raise Exception("Read: no hay datos")
            dataBytes[pos] = b[0]
            pos = pos + 1
        return bytes(dataBytes)

    def readLine(self, maxChars)->str:
        """Lee una linea de texto finalizada en NL.

        'maxChars' especifica el máximo número de caracteres a leer.
        El caracter NL no es incluido en la linea retornada
        """
        linea = ''
        pos = 0
        while(pos < maxChars + 1):
            b = self.serial.read(1)
            if( len(b) == 0 ):
                raise Exception("Readline: no hay datos")
            if(b[0]==10):
                return linea
            linea =linea + chr(b[0])
        raise Exception("ReadLine: no hay newline")

    def ignoreInput(self, timex:int)->None:
        """Descarta durante 'timex' ms los datos presentes para lectura."""
        timeout = self.serial.timeout
        self.serial.timeout = 0
        t = time.time()
        end = t + timex/1000.0
        while(t < end):
            if( self.serial.in_waiting>0):
                self.serial.read(1)
            else:
                time.sleep(0.010)
            t = time.time()
        self.serial.timeout = timeout

    def setDTR(self, value:bool)->None:
        """Activa/desactiva la linea DTR."""
        self.serial.setDTR(value)
