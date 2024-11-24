"""Acceso a todas las funcionalidades del Scribbler2 (S2)."""

import time
import serial

from scribbler2.S2.HEncoders import HEncoders
from scribbler2.S2.HInfrared import HInfrared
from scribbler2.S2.HLights import HLights
from scribbler2.S2.HLineSensors import HLineSensors
from scribbler2.S2.HMotorStats import HMotorStats
from scribbler2.S2.HSensors import HSensors
from scribbler2.S2.HState import HState


class Robot(object):
    """Clase para base interactuar con un Scribbler2 via conexion serial."""

    DATA_LENGTH = 8
    PACKET_LENGTH = 9

    def __init__(
        self,
        port: str,
        baudrate: int = 38400,
        timeout: float = 1.0,
        delay: float = 3.0,
    ) -> None:
        """Inicializa el objeto y lo conecta al S2."""
        self.conn = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

        # el S2 se resetea y debemos esperar a que este listo
        time.sleep(delay)

        # limpiamos cualquier residuo
        self.flushBuffers()

    def flushBuffers(self) -> None:
        """Limpia los buffers de entrada y salida de la puerta serial."""
        self.conn.reset_output_buffer()
        self.conn.reset_input_buffer()
        self.conn.read(1000)

    def setDTR(self, dtr: bool, delay: float = 0.001) -> None:
        """Manipula la linea DTR para el robot."""
        self.conn.setDTR(dtr)
        time.sleep(delay)

    def setTimeout(self, timeout: float) -> None:
        """Establece el timeout para la entrada y salida."""
        self.conn.timeout = timeout

    def close(self) -> None:
        """Cierra la conexion hacia el S2."""
        self.conn.close()

    def reset(self, delay: float = 3.0) -> None:
        """Resetea el S2 por software"""
        packet = self._makeS2Packet(33)
        self._sendS2Command(packet)
        time.sleep(delay)
        self.flushBuffers()

    def getInfo(self) -> str:
        """Obtiene datos informativos del S2."""
        packet = self._makeS2Packet(80)
        self._sendS2Command(packet)
        return self._getLineResponse(128)

    def getPass(self) -> str:
        """Obtiene la clave actualmente almacenada en el S2."""
        packet = self._makeS2Packet(50)
        self._sendS2Command(packet)
        pass1 = self._getBytesResponse(8)
        packet[0] = 51
        self._sendS2Command(packet)
        pass2 = self._getBytesResponse(8)
        return (pass1 + pass2).decode("ascii")

    def getName(self) -> str:
        """Obtiene el nombre del S2."""
        packet = self._makeS2Packet(78)
        self._sendS2Command(packet)
        name1 = self._getBytesResponse(8)
        packet[0] = 64
        self._sendS2Command(packet)
        name2 = self._getBytesResponse(8)
        return (name1 + name2).decode("ascii")

    def getState(self) -> HState:
        """Obtiene estado del S2."""
        packet = self._makeS2Packet(77)
        self._sendS2Command(packet)
        return HState(self._getUInt8Response(), self._getUInt8Response())

    def getData(self) -> bytes:
        """Obtiene data almacenada en el S2."""
        packet = self._makeS2Packet(81)
        self._sendS2Command(packet)
        return self._getBytesResponse(self.DATA_LENGTH)

    def setPass(self, passw: str) -> HSensors:
        """Establece la clave ('passwd') a almacenar en el S2."""
        bpass = passw.encode("ascii")
        packet = self._makeS2Packet(55)
        i = 0
        while i < len(bpass) and i < self.DATA_LENGTH:
            packet[i + 1] = bpass[i]
            i = i + 1
        while i < self.DATA_LENGTH:
            packet[i + 1] = 32
            i = i + 1
        self._sendS2Command(packet)
        self._getS2SensorsResponse()

        packet[0] = 56
        j = 0
        while i < len(bpass) and j < self.DATA_LENGTH:
            packet[j + 1] = bpass[i]
            i = i + 1
            j = j + 1
        while j < self.DATA_LENGTH:
            packet[j + 1] = 32
            j = j + 1
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setSingleData(self, pos: int, data: int) -> HSensors:
        """Almacena un dato en el S2.

        El dato (0 a 255) es almacenado en la zona de almacenamiento interno
        del S2 en la posicion dada por 'pos' (0 a 8)
        """
        packet = self._makeS2Packet(96)
        packet[1] = pos & 0x07
        packet[2] = data & 0xFF
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setData(self, data: list) -> HSensors:
        """Almacena un grupo de datos (8) en la zona interna del S2."""
        packet = self._makeS2Packet(97)
        i = 0
        while i < len(data) and i < self.DATA_LENGTH:
            packet[i + 1] = data[i]
            i = i + 1
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setName(self, name: str) -> HSensors:
        """Establece el nombre del S2."""
        bname = name.encode("ascii")
        packet = self._makeS2Packet(110)
        i = 0
        while i < len(bname) and i < self.DATA_LENGTH:
            packet[i + 1] = bname[i]
            i = i + 1
        while i < self.DATA_LENGTH:
            packet[i + 1] = 32
            i = i + 1
        self._sendS2Command(packet)
        self._getS2SensorsResponse()

        packet[0] = 119
        j = 0
        while i < len(bname) and j < self.DATA_LENGTH:
            packet[j + 1] = bname[i]
            i = i + 1
            j = j + 1
        while j < self.DATA_LENGTH:
            packet[j + 1] = 32
            j = j + 1
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def getAllSensors(self) -> HSensors:
        """Obtiene el valor de los principales sensores del S2."""
        packet = self._makeS2Packet(65)
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def getIRLeft(self) -> int:
        """Obtiene valor del sensor IR izquierdo."""
        packet = self._makeS2Packet(71)
        self._sendS2Command(packet)
        return self._getUInt8Response()

    def getIRRight(self) -> int:
        """Obtiene valor del sensor IR derecho."""
        packet = self._makeS2Packet(72)
        self._sendS2Command(packet)
        return self._getUInt8Response()

    def getAllIR(self) -> HInfrared:
        """Obtiene el valor de todos los sensores IR del S2."""
        packet = self._makeS2Packet(73)
        self._sendS2Command(packet)
        return HInfrared(self._getUInt8Response(), self._getUInt8Response())

    def getIrEx(self, sensor: int, umbral: int) -> int:
        """Obtiene el valor extendido de un sensor (0-1) infrarojo del S2."""
        packet = self._makeS2Packet(172)
        packet[1] = sensor & 0x01
        packet[2] = 0
        packet[3] = umbral & 0xFF
        self._sendS2Command(packet)
        return self._getUInt8Response()

    def getDistanceEx(self, sensor: int) -> int:
        """Obtiene la distacia medida por un sensor (0-1)."""
        packet = self._makeS2Packet(175)
        packet[1] = sensor & 0x01
        self._sendS2Command(packet)
        return self._getUInt8Response()

    def setLeftLed(self, encender: bool) -> HSensors:
        """Enciende o apaga el LED izquierdo."""
        cmd = 100
        if encender:
            cmd = 99
        packet = self._makeS2Packet(cmd)
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setCenterLed(self, encender: bool) -> HSensors:
        """Enciende o apaga el LED central."""
        cmd = 102
        if encender:
            cmd = 101
        packet = self._makeS2Packet(cmd)
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setRightLed(self, encender: bool) -> HSensors:
        """Enciende o apaga el LED derecho."""
        cmd = 104
        if encender:
            cmd = 103
        packet = self._makeS2Packet(cmd)
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setAllLed(self, left: bool, center: bool, right: bool) -> HSensors:
        """Enciende y/o apaga los LEDs del S2."""
        packet = self._makeS2Packet(107)
        packet[1] = left & 0x01
        packet[2] = center & 0x01
        packet[3] = right & 0x01
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def getLeftLight(self) -> int:
        """Obtiene el valor del sensor de luz izquierdo."""
        packet = self._makeS2Packet(67)
        self._sendS2Command(packet)
        return self._getUInt16Response()

    def getCenterLight(self) -> int:
        """Obtiene el valor del sensor de luz central."""
        packet = self._makeS2Packet(68)
        self._sendS2Command(packet)
        return self._getUInt16Response()

    def getRightLight(self) -> int:
        """Obtiene el valor del sensor de luz derecho."""
        packet = self._makeS2Packet(69)
        self._sendS2Command(packet)
        return self._getUInt16Response()

    def getAllLights(self) -> HLights:
        """Obtiene el valor de los sensores de luz."""
        packet = self._makeS2Packet(70)
        self._sendS2Command(packet)
        return HLights(
            self._getUInt16Response(),
            self._getUInt16Response(),
            self._getUInt16Response(),
        )

    def getLeftLine(self) -> int:
        """Obtiene el valor del sensor de linea izquierdo."""
        packet = self._makeS2Packet(74)
        self._sendS2Command(packet)
        return self._getUInt8Response()

    def getRightLine(self) -> int:
        """Obtiene el valor del sensor de linea derecho."""
        packet = self._makeS2Packet(75)
        self._sendS2Command(packet)
        return self._getUInt8Response()

    def getAllLines(self) -> HLineSensors:
        """Obtiene el valor de los sensores de linea del S2."""
        packet = self._makeS2Packet(76)
        self._sendS2Command(packet)
        return HLineSensors(self._getUInt8Response(), self._getUInt8Response())

    def getLineEx(self, sensor: int, umbral: int) -> int:
        """Obtiene el valor extendido de un sensor (o-1) de linea."""
        packet = self._makeS2Packet(173)
        packet[1] = sensor & 0x01
        packet[2] = 0
        packet[3] = umbral & 0xFF
        self._sendS2Command(packet)
        return self._getUInt8Response()

    def getMicEnv(self) -> int:
        """Obtiene el valor del microfono del S2."""
        packet = self._makeS2Packet(169)
        self._sendS2Command(packet)
        return self._getUInt32Response()

    def getMotorStats(self) -> HMotorStats:
        """Obtiene el estado de los motores del S2."""
        packet = self._makeS2Packet(170)
        self._sendS2Command(packet)
        return HMotorStats(self._getUInt32Response(), self._getUInt8Response())

    def getEncoders(self, preserve: int) -> HEncoders:
        """Obtiene estado de los encoders del S2.

        'preserve' indica si se conserva (1) o borra (0) el valor de los
        encoder al leer
        """
        packet = self._makeS2Packet(171)
        packet[1] = preserve & 0x01
        self._sendS2Command(packet)
        return HEncoders(self._getUInt32Response(), self._getUInt32Response())

    def getStall(self) -> int:
        """Obtiene estado de las ruedas (atrapadas o no)."""
        packet = self._makeS2Packet(79)
        self._sendS2Command(packet)
        return self._getUInt8Response()

    def setMotorsOff(self) -> HSensors:
        """Apaga los motores del S2."""
        packet = self._makeS2Packet(108)
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setMotors(self, left: int = 0, right: int = 0) -> HSensors:
        """Enciende los motores del S2.

        'left' es el porcentaje de potencia para el motor izquierdo (-100 a 100)
        'right' es el porcentaje de potencia para el motor derecho (-100 a 100)
        """
        left = int(left)
        if left > 100:
            left = 100
        elif left < -100:
            left = -100
        left = left + 100

        right = int(right)
        if right > 100:
            right = 100
        elif right < -100:
            right = -100
        right = right + 100

        packet = self._makeS2Packet(109)
        packet[1] = right
        packet[2] = left
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setQuiet(self) -> HSensors:
        """Apaga el parlante del S2."""
        packet = self._makeS2Packet(112)
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setLoud(self) -> HSensors:
        """Activa el parlante del S2."""
        packet = self._makeS2Packet(111)
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setVolume(self, volume: int) -> HSensors:
        """Establece porcentaje del nivel de volumen del parlante del S2.

        'volume' corresponde al porcentaje de volumen (0 a 100) del parlante
        """
        volume = volume & 0xFF
        if volume > 100:
            volume = 100
        packet = self._makeS2Packet(160)
        packet[1] = volume
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setSpeaker(self, duration: int, freq1: int, freq2: int = 0) -> HSensors:
        """Genera sonido a traves del parlante del S2.

        'duration' es la duracion del sonido en ms (no superior a 2500)
        'freq1' es la frecuencia principal en Hz
        'freq2' es la frecuencia secundaria en Hz
        """
        duration = duration & 0xFFFF
        if duration > 2500:
            duration = 2500
        freq1 = freq1 & 0xFFFF
        freq2 = freq2 & 0xFFFF
        packet = self._makeS2Packet(114)
        packet[1] = (duration >> 8) & 0xFF
        packet[2] = duration & 0xFF
        packet[3] = (freq1 >> 8) & 0xFF
        packet[4] = freq1 & 0xFF
        packet[5] = (freq2 >> 8) & 0xFF
        packet[6] = freq2 & 0xFF
        self._sendS2Command(packet, duration)
        return self._getS2SensorsResponse()

    # ----
    # metodos para mover al robot en un plano cartesiano
    # ----

    def beginPath(self, speed: int) -> HSensors:
        """Coloca al S2 en modo de desplazamiento en sistema cartesiano (path).

        'speed' es la velocidad de desplazamiento (0 a 15)
        """
        packet = self._makeS2Packet(161)
        packet[1] = 1
        packet[2] = 0
        packet[3] = speed & 0x0F
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def endPath(self) -> HSensors:
        """Finaliza el modo path."""
        packet = self._makeS2Packet(161)
        packet[1] = 0
        self._sendS2PathCommand(packet)
        return self._getS2SensorsResponse()

    def getPosn(self) -> tuple:
        """Obtiene ubicacion (x, y) del S2 en el plano cartesiano."""
        packet = self._makeS2Packet(165)
        self._sendS2Command(packet)
        return (self._getInt32Response(), self._getInt32Response())

    def getAngle(self) -> int:
        """Obtiene angulo en el que se encuentra orientado el S2."""
        packet = self._makeS2Packet(167)
        self._sendS2Command(packet)
        return self._getInt32Response()

    def setPosn(self, x: int, y: int) -> HSensors:
        """Establece posicion (x, y) del S2 en el plano (no lo desplaza)."""
        packet = self._makeS2Packet(166)
        packet[1] = (x >> 24) & 0xFF
        packet[2] = (x >> 16) & 0xFF
        packet[3] = (x >> 8) & 0xFF
        packet[4] = x & 0xFF
        packet[5] = (y >> 24) & 0xFF
        packet[6] = (y >> 16) & 0xFF
        packet[7] = (y >> 8) & 0xFF
        packet[8] = y & 0xFF
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def setAngle(self, angle: int) -> HSensors:
        """Establece angulo de orientacion del S2 (no lo desplaza)."""
        packet = self._makeS2Packet(168)
        packet[1] = (angle >> 24) & 0xFF
        packet[2] = (angle >> 16) & 0xFF
        packet[3] = (angle >> 8) & 0xFF
        packet[4] = angle & 0xFF
        self._sendS2Command(packet)
        return self._getS2SensorsResponse()

    def moveTo(self, x: int, y: int) -> HSensors:
        """Desplaza el S2 a la posicion (x, y)."""
        packet = self._makeS2Packet(162)
        packet[1] = 2 + 1
        packet[2] = (x >> 8) & 0xFF
        packet[3] = x & 0xFF
        packet[4] = (y >> 8) & 0xFF
        packet[5] = y & 0xFF
        self._sendS2PathCommand(packet)
        return self._getS2SensorsResponse()

    def moveBy(self, x: int, y: int) -> HSensors:
        """Desplaza de manera relativa el S2 una distancia de (x, y)."""
        packet = self._makeS2Packet(162)
        packet[1] = 4 + 1
        packet[2] = (x >> 8) & 0xFF
        packet[3] = x & 0xFF
        packet[4] = (y >> 8) & 0xFF
        packet[5] = y & 0xFF
        self._sendS2PathCommand(packet)
        return self._getS2SensorsResponse()

    def turnTo(self, angle: int) -> HSensors:
        """Mueve al S2 orientandolo a un angulo dado."""
        packet = self._makeS2Packet(164)
        packet[1] = 2 + 1
        packet[2] = (angle >> 8) & 0xFF
        packet[3] = angle & 0xFF
        self._sendS2PathCommand(packet)
        return self._getS2SensorsResponse()

    def turnBy(self, angle: int) -> HSensors:
        """Gira de manera relativa el S2 un numero dado de grados."""
        packet = self._makeS2Packet(164)
        packet[1] = 4 + 1
        packet[2] = (angle >> 8) & 0xFF
        packet[3] = angle & 0xFF
        self._sendS2PathCommand(packet)
        return self._getS2SensorsResponse()

    def arcTo(self, x: int, y: int, radius: int) -> HSensors:
        """Traza un arco hasta la posicion (x, y) de radio dado."""
        packet = self._makeS2Packet(163)
        packet[1] = 2 + 1
        packet[2] = (x >> 8) & 0xFF
        packet[3] = x & 0xFF
        packet[4] = (y >> 8) & 0xFF
        packet[5] = y & 0xFF
        packet[6] = (radius >> 8) & 0xFF
        packet[7] = radius & 0xFF
        self._sendS2PathCommand(packet)
        return self._getS2SensorsResponse()

    def arcBy(self, x: int, y: int, radius: int) -> HSensors:
        """Traza un arco de manera relativa y de radio dado."""
        packet = self._makeS2Packet(163)
        packet[1] = 4 + 1
        packet[2] = (x >> 8) & 0xFF
        packet[3] = x & 0xFF
        packet[4] = (y >> 8) & 0xFF
        packet[5] = y & 0xFF
        packet[6] = (radius >> 8) & 0xFF
        packet[7] = radius & 0xFF
        self._sendS2PathCommand(packet)
        return self._getS2SensorsResponse()

    ## protected -------------------------------

    def _makeS2Packet(self, cmd: int) -> bytearray:
        """Crea un paquete estandar utilizado como comando para el S2."""
        packet = bytearray(self.PACKET_LENGTH)
        packet[0] = cmd & 0xFF
        return packet

    def _sendS2Command(self, packet: bytearray, pause: int = 0) -> bool:
        """Envia un comando al S2.

        'pause' especifica el tiempo en ms a esperar por la respuesta luego
        de enviar el comando
        """
        self.conn.write(packet)
        self.conn.flush()
        if pause > 0:
            time.sleep(pause / 1000.0)

        # recibe el echo
        if packet[0] != 0x50:  # GetInfo no da echo
            if packet[0] != 0x21:  # SoftReset da echo parcial
                b = self.conn.read(self.PACKET_LENGTH)
                if packet != b:
                    print("Packet Mismatch:")
                    return False
        return True

    def _sendS2PathCommand(self, packet: bytearray) -> None:
        """Envia comando de desplazamiento (en modo path) al S2."""
        self.conn.write(packet)
        self.conn.flush()

        # recibe el echo
        b = self.conn.read(self.PACKET_LENGTH)
        if packet != b:
            print("Packet Mismatch (path):")

        # recibe la respuesta del comando
        self._getS2SensorsResponse()

        # espera a que los motores se detengan
        packet = self._makeS2Packet(170)
        while True:
            self._sendS2Command(packet)
            stat = HMotorStats(self._getUInt32Response(), self._getUInt8Response())
            moving = (stat.stat & 0x03) != 0  # or stat.moveReady==0
            if moving:
                time.sleep(0.5)
            else:
                break

        # dejamosla respuesta apropiada para ser leida por quien invoca
        packet = self._makeS2Packet(65)
        self._sendS2Command(packet)

    def _getS2SensorsResponse(self) -> HSensors:
        """Obtiene estado de los principales sensores del S2."""
        return HSensors(
            self._getUInt8Response(),
            self._getUInt8Response(),
            self._getUInt16Response(),
            self._getUInt16Response(),
            self._getUInt16Response(),
            self._getUInt8Response(),
            self._getUInt8Response(),
            self._getUInt8Response(),
        )

    def _getLineResponse(self, max_chars: int) -> str:
        """Obtiene una respuesta del S2 como un string ascii."""
        linea = ""
        pos = 0
        while pos < max_chars + 1:
            b = self.conn.read(1)
            if b == b"":
                continue
            if b[0] == 10:
                break
            linea = linea + chr(b[0])
        return linea

    def _getUInt8Response(self) -> int:
        """Obtiene una respuesta del S2 como un entero de 8 bits sin signo."""
        b = self.conn.read(1)
        return b[0] & 0xFF

    def _getUInt16Response(self) -> int:
        """Obtiene una respuesta del S2 como un entero de 16 bits sin signo."""
        b = self.conn.read(2)
        n = b[0] & 0x000000FF
        n = (n << 8) | (b[1] & 0xFF)
        return n

    def _getUInt32Response(self) -> int:
        """Obtiene una respuesta del S2 como un entero de 32 bits sin signo."""
        b = self.conn.read(4)
        n = b[0] & 0x000000FF
        n = (n << 8) | (b[1] & 0xFF)
        n = (n << 8) | (b[2] & 0xFF)
        n = (n << 8) | (b[3] & 0xFF)
        if (n & 0x80000000) != 0:
            return n - 0xFFFFFFFF - 1
        else:
            return n

    def _getInt32Response(self) -> int:
        """Obtiene una respuesta del S2 como un entero de 32 bits con signo."""
        n = self._getUInt32Response()
        return int(n)

    def _getBytesResponse(self, nbytes: int) -> bytes:
        """Obtiene una respuesta del S2 como un conjunto de bytes."""
        return self.conn.read(nbytes)
