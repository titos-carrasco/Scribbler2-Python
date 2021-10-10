# -*- coding: utf-8 -*-

"""Acceso a todas las funcionalidades del Scribbler2 (S2)."""

import threading
import time

from scribbler2.robot.HS2Sensors import HS2Sensors
from scribbler2.robot.HS2State import HS2State
from scribbler2.robot.HS2Infrared import HS2Infrared
from scribbler2.robot.HS2Lights import HS2Lights
from scribbler2.robot.HS2LineSensors import HS2LineSensors
from scribbler2.robot.HS2MotorStats import HS2MotorStats
from scribbler2.robot.HS2Encoders import HS2Encoders
from scribbler2.robot.ISerial import ISerial

class Scribbler2(object):
    """Clase para base interactuar con un Scribbler2."""

    DATA_LENGTH = 8
    PACKET_LENGTH = 9

    def __init__(self, conn:ISerial)->None:
        """Inicializa el objeto y lo conecta al S2."""
        self.mylock = threading.Lock()
        self.conn = conn
        self.conn.ignoreInput(1000)

    def close(self)->None:
        """Cierra la conexion hacia el S2."""
        try:
            self._lock()
            self.conn.close()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getInfo(self)->str:
        """Obtiene datos informativos del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(80)
            self._sendS2Command(packet, 0)
            return self._getLineResponse(128)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getPass(self)->str:
        """Obtiene la clave actualmente almacenada en el S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(50)
            self._sendS2Command(packet, 0)
            pass1 = self._getBytesResponse(8)
            packet[0] = 51
            self._sendS2Command(packet, 0)
            pass2 = self._getBytesResponse(8)
            return (pass1 + pass2).decode('ascii')
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getName(self)->str:
        """Obtiene el nombre del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(78)
            self._sendS2Command(packet, 0)
            name1 = self._getBytesResponse(8)
            packet[0] = 64
            self._sendS2Command(packet, 0)
            name2 = self._getBytesResponse(8)
            return (name1 + name2).decode('ascii')
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getState(self)->HS2State:
        """Obtiene estado del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(77)
            self._sendS2Command(packet, 0)
            return HS2State(self._getUInt8Response(), self._getUInt8Response())
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getData(self)->bytearray:
        """Obtiene data almacenada en el S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(81)
            self._sendS2Command(packet, 0)
            return self._getBytesResponse(self.DATA_LENGTH)
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setPass(self, passw:str)->HS2Sensors:
        """Establece la clave ('passwd') a almacenar en el S2."""
        try:
            self._lock()
            bPass = passw.encode('ascii')
            packet = self._makeS2Packet(55)
            i = 0
            while(i<len(bPass) and i<self.DATA_LENGTH):
                packet[i+1] = bPass[i]
                i = i + 1
            while(i<self.DATA_LENGTH):
                packet[i+1] = 32
                i = i + 1
            self._sendS2Command(packet, 0)
            self._getS2SensorsResponse()

            packet[0] = 56
            j = 0
            while(i<len(bPass) and j<self.DATA_LENGTH):
                packet[j+1] = bPass[i]
                i = i + 1
                j = j + 1
            while(j<self.DATA_LENGTH):
                packet[j+1] = 32
                j = j + 1
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setSingleData(self, pos:int, data:int)->HS2Sensors:
        """Almacena un dato en el S2.

        El dato (0 a 255) es almacenado en la zona de almacenamiento interno
        del S2 en la posicion dada por 'pos' (0 a 8)
        """
        try:
            self._lock()
            packet = self._makeS2Packet(96)
            packet[1] = pos & 0x07
            packet[2] = data & 0xFF
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setData(self, data:list)->HS2Sensors:
        """Almacena un grupo de datos (8) en la zona interna del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(97)
            i = 0
            while(i<len(data) and  i<self.DATA_LENGTH):
                packet[i+1] = data[i]
                i = i + 1
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setName(self,  name:str)->HS2Sensors:
        """Establece el nombre del S2."""
        try:
            self._lock()
            bName = name.encode('ascii')
            packet = self._makeS2Packet(110)
            i = 0
            while(i<len(bName) and i<self.DATA_LENGTH):
                packet[i+1] = bName[i]
                i = i + 1
            while(i<self.DATA_LENGTH):
                packet[i+1] = 32
                i = i + 1
            self._sendS2Command(packet, 0)
            self._getS2SensorsResponse()

            packet[0] = 119
            j = 0
            while(i<len(bName) and j<self.DATA_LENGTH):
                packet[j+1] = bName[i]
                i = i + 1
                j = j + 1
            while(j<self.DATA_LENGTH):
                packet[j+1] = 32
                j = j + 1
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getAllSensors(self)->HS2Sensors:
        """Obtiene el valor de los principales sensores del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(65)
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getIRLeft(self)->int:
        """Obtiene valor del sensor IR izquierdo."""
        try:
            self._lock()
            packet = self._makeS2Packet(71)
            self._sendS2Command(packet, 0)
            return self._getUInt8Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getIRRight(self)->int:
        """Obtiene valor del sensor IR derecho."""
        try:
            self._lock()
            packet = self._makeS2Packet(72)
            self._sendS2Command(packet, 0)
            return self._getUInt8Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getAllIR(self)->HS2Infrared:
        """Obtiene el valor de todos los sensores IR del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(73)
            self._sendS2Command(packet, 0)
            return HS2Infrared(self._getUInt8Response(), self._getUInt8Response())
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getIrEx(self, sensor:int, umbral:int)->int:
        """Obtiene el valor extendido de un sensor (0-1) infrarojo del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(172)
            packet[1] = sensor & 0x01
            packet[2] = 0
            packet[3] = umbral & 0xFF
            self._sendS2Command(packet, 0)
            return self._getUInt8Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getDistanceEx(self, sensor:int)->int:
        """Obtiene la distacia medida por un sensor (0-1)."""
        try:
            self._lock()
            packet = self._makeS2Packet(175)
            packet[1] = sensor & 0x01
            self._sendS2Command(packet, 0)
            return self._getUInt8Response()
        except Exception as e:
            raise
        finally:
            self._unlock()


    def setLeftLed(self, encender:bool)->HS2Sensors:
        """Enciende o apaga el LED izquierdo."""
        try:
            self._lock()
            cmd = 100
            if(encender):
                cmd = 99
            packet = self._makeS2Packet(cmd)
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setCenterLed(self, encender:bool)->HS2Sensors:
        """Enciende o apaga el LED central."""
        try:
            self._lock()
            cmd = 102
            if(encender):
                cmd = 101
            packet = self._makeS2Packet(cmd)
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setRightLed(self, encender:bool)->HS2Sensors:
        """Enciende o apaga el LED derecho."""
        try:
            self._lock()
            cmd = 104
            if(encender):
                cmd = 103
            packet = self._makeS2Packet(cmd)
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setAllLed(self, left:bool, center:bool, right:bool)->HS2Sensors:
        """Enciende y/o apaga los LEDs del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(107)
            packet[1] = left & 0x01
            packet[2] = center & 0x01
            packet[3] = right & 0x01
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getLeftLight(self)->int:
        """Obtiene el valor del sensor de luz izquierdo."""
        try:
            self._lock()
            packet = self._makeS2Packet(67)
            self._sendS2Command(packet, 0)
            return self._getUInt16Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getCenterLight(self)->int:
        """Obtiene el valor del sensor de luz central."""
        try:
            self._lock()
            packet = self._makeS2Packet(68)
            self._sendS2Command(packet, 0)
            return self._getUInt16Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getRightLight(self)->int:
        """Obtiene el valor del sensor de luz derecho."""
        try:
            self._lock()
            packet = self._makeS2Packet(69)
            self._sendS2Command(packet, 0)
            return self._getUInt16Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getAllLights(self)->HS2Lights:
        """Obtiene el valor de los sensores de luz."""
        try:
            self._lock()
            packet = self._makeS2Packet(70)
            self._sendS2Command(packet, 0)
            return HS2Lights(self._getUInt16Response(), self._getUInt16Response(), self._getUInt16Response())
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getLeftLine(self)->int:
        """Obtiene el valor del sensor de linea izquierdo."""
        try:
            self._lock()
            packet = self._makeS2Packet(74)
            self._sendS2Command(packet, 0)
            return self._getUInt8Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getRightLine(self)->int:
        """Obtiene el valor del sensor de linea derecho."""
        try:
            self._lock()
            packet = self._makeS2Packet(75)
            self._sendS2Command(packet, 0)
            return self._getUInt8Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getAllLines(self)->HS2LineSensors:
        """Obtiene el valor de los sensores de linea del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(76)
            self._sendS2Command(packet, 0)
            return HS2LineSensors(self._getUInt8Response(), self._getUInt8Response())
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getLineEx(self, sensor:int, umbral:int)->int:
        """Obtiene el valor extendido de un sensor (o-1) de linea."""
        try:
            self._lock()
            packet = self._makeS2Packet(173)
            packet[1] = sensor & 0x01
            packet[2] = 0
            packet[3] = umbral & 0xFF
            self._sendS2Command(packet, 0)
            return self._getUInt8Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getMicEnv(self)->int:
        """Obtiene el valor del microfono del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(169)
            self._sendS2Command(packet, 0)
            return self._getUInt32Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getMotorStats(self)->HS2MotorStats:
        """Obtiene el estado de los motores del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(170)
            self._sendS2Command(packet, 0)
            return HS2MotorStats(self._getUInt32Response(), self._getUInt8Response())
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getEncoders(self, preserve:int)->HS2Encoders:
        """Obtiene estado de los encoders del S2.

        'preserve' indica si se conserva (1) o borra (0) el valor de los
        encoder al leer
        """
        try:
            self._lock()
            packet = self._makeS2Packet(171)
            packet[1] = preserve & 0x01
            self._sendS2Command(packet, 0)
            return HS2Encoders(self._getUInt32Response(), self._getUInt32Response())
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getStall(self)->int:
        """Obtiene estado de las ruedas (atrapadas o no)."""
        try:
            self._lock()
            packet = self._makeS2Packet(79)
            self._sendS2Command(packet, 0)
            return self._getUInt8Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setMotorsOff(self)->HS2Sensors:
        """Apaga los motores del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(108)
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setMotors(self, left:int, right:int)->HS2Sensors:
        """Enciende los motores del S2.

        'left' es el porcentaje de potencia para el motor izquierdo (-100 a 100)
        'right' es el porcentaje de potencia para el motor derecho (-100 a 100)
        """
        try:
            self._lock()
            if(left>100):
                left = 100
            elif(left<-100):
                left = -100
            left = left + 100

            if(right>100):
                right = 100
            elif(right<-100):
                right = -100
            right = right + 100

            packet = self._makeS2Packet(109)
            packet[1] = int(right)
            packet[2] = int(left)
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setQuiet(self)->HS2Sensors:
        """Apaga el parlante del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(112)
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setLoud(self)->HS2Sensors:
        """Activa el parlante del S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(111)
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setVolume(self, volume:int)->HS2Sensors:
        """Establece porcentaje del nivel de volumen del parlante del S2.

        'volume' corresponde al porcentaje de volumen (0 a 100) del parlante
        """
        try:
            self._lock()
            volume = volume & 0xFF
            if(volume > 100):
                volume= 100
            packet = self._makeS2Packet(160)
            packet[1] = volume
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setSpeaker(self, duration:int, freq1:int, freq2:int=0)->HS2Sensors:
        """Genera sonido a traves del parlante del S2.

        'duration' es la duracion del sonido en ms (no superior a 2500)
        'freq1' es la frecuencia principal en Hz
        'freq2' es la frecuencia secundaria en Hz
        """
        try:
            self._lock()
            duration = duration & 0xFFFF
            if(duration > 2500):
                duration = 2500
            freq1 = freq1 & 0xFFFF
            freq2 = freq2 & 0xFFFF
            packet = self._makeS2Packet(114)
            packet[1] = (duration >>8) & 0xFF
            packet[2] = duration & 0xFF
            packet[3] = (freq1 >> 8) & 0xFF
            packet[4] = freq1 & 0xFF
            packet[5] = (freq2 >> 8) & 0xFF
            packet[6] = freq2 & 0xFF
            self._sendS2Command(packet, duration/1000.0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    # metodos para mover al robot en un plano cartesiano

    def beginPath(self, speed:int)->HS2Sensors:
        """Colocal al S2 en modo de desplazamiento en sistema cartesiano (path).

        'speed' es la velocidad de desplazamiento (0 a 15)
        """
        try:
            self._lock()
            packet = self._makeS2Packet(161)
            packet[1] = 1
            packet[2] = 0
            packet[3] = speed & 0x0F
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def endPath(self)->HS2Sensors:
        """Finaliza el modo path."""
        try:
            self._lock()
            packet = self._makeS2Packet(161)
            packet[1] = 0
            self._sendS2PathCommand(packet)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getPosn(self)->tuple:
        """Obtiene ubicacion (x, y) del S2 en el plano cartesiano."""
        try:
            self._lock()
            packet = self._makeS2Packet(165)
            self._sendS2Command(packet, 0)
            return (self._getInt32Response(), self._getInt32Response())
        except Exception as e:
            raise
        finally:
            self._unlock()

    def getAngle(self)->int:
        """Obtiene angulo en el que se encuentra orientado el S2."""
        try:
            self._lock()
            packet = self._makeS2Packet(167)
            self._sendS2Command(packet, 0)
            return self._getInt32Response()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setPosn(self, x:int, y:int)->HS2Sensors:
        """Establece posicion (x, y) del S2 en el plano (no lo desplaza)."""
        try:
            self._lock()
            packet = self._makeS2Packet(166)
            packet[1] = (x >> 24) & 0xFF
            packet[2] = (x >> 16) & 0xFF
            packet[3] = (x >> 8) & 0xFF
            packet[4] = x & 0xFF
            packet[5] = (y >> 24) & 0xFF
            packet[6] = (y >> 16) & 0xFF
            packet[7] = (y >> 8) & 0xFF
            packet[8] = y & 0xFF
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def setAngle(self, angle:int)->HS2Sensors:
        """Establece angulo de orientacion del S2 (no lo desplaza)."""
        try:
            self._lock()
            packet = self._makeS2Packet(168)
            packet[1] = (angle >> 24) & 0xFF
            packet[2] = (angle >> 16) & 0xFF
            packet[3] = (angle >> 8) & 0xFF
            packet[4] = angle & 0xFF
            self._sendS2Command(packet, 0)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def moveTo(self, x:int, y:int)->HS2Sensors:
        """Desplaza el S2 a la posicion (x, y)."""
        try:
            self._lock()
            packet = self._makeS2Packet(162)
            packet[1] = 2 + 1
            packet[2] = (x >> 8) & 0xFF
            packet[3] = x & 0xFF
            packet[4] = (y >> 8) & 0xFF
            packet[5] = y & 0xFF
            self._sendS2PathCommand(packet)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def moveBy(self, x:int, y:int)->HS2Sensors:
        """Desplaza de manera relativa el S2 una distancia de (x, y)."""
        try:
            self._lock()
            packet = self._makeS2Packet(162)
            packet[1] = 4 + 1
            packet[2] = (x >> 8) & 0xFF
            packet[3] = x & 0xFF
            packet[4] = (y >> 8) & 0xFF
            packet[5] = y & 0xFF
            self._sendS2PathCommand(packet)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def turnTo(self, angle:int)->HS2Sensors:
        """Mueve al S2 orientandolo a un angulo dado."""
        try:
            self._lock()
            packet = self._makeS2Packet(164)
            packet[1] = 2 + 1
            packet[2] = (angle >> 8) & 0xFF
            packet[3] = angle & 0xFF
            self._sendS2PathCommand(packet)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def turnBy(self, angle:int)->HS2Sensors:
        """Gira de manera relativa el S2 un numero dado de grados."""
        try:
            self._lock()
            packet = self._makeS2Packet(164)
            packet[1] = 4 + 1
            packet[2] = (angle >> 8) & 0xFF
            packet[3] = angle & 0xFF
            self._sendS2PathCommand(packet)
            return self._getS2SensorsResponse()
        except Exception as e:
            raise
        finally:
            self._unlock()

    def arcTo(self, x:int, y:int, radius:int)->HS2Sensors:
        """Traza un arco hasta la posicion (x, y) de radio dado."""
        try:
            self._lock()
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
        except Exception as e:
            raise
        finally:
            self._unlock()

    def arcBy(self, x:int, y:int, radius:int)->HS2Sensors:
        """Traza un arco de manera relativa y de radio dado."""
        try:
            self._lock()
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
        except Exception as e:
            raise
        finally:
            self._unlock()

    ## protected -------------------------------

    def _makeS2Packet(self, cmd:int)->bytearray:
        """Crea un paquete estandar utilizado como comando para el S2."""
        packet = bytearray(self.PACKET_LENGTH)
        packet[0] = cmd & 0xFF
        return packet

    def _sendS2Command(self, packet:bytearray, pause:int=0)->bool:
        """Envia un comando al S2.

        'pause' especifica el tiempo en ms a esperar por la respuesta luego
        de enviar el comando
        """
        self.conn.write(packet)
        if(pause > 0):
            time.sleep(pause)
        if(packet[0] != 0x50):
            b = self.conn.read(self.PACKET_LENGTH)
            if(packet != b):
                print("Packet Mismatch:")
                return False
        return True

    def _sendS2PathCommand(self, packet:bytearray)->None:
        """Envia comando de trazado (path) al S2."""
        self.conn.write(packet)
        t = time.time()
        while(time.time() - t  < 3.5):
            try:
                b = self.conn.read(self.PACKET_LENGTH)
                if(packet != b):
                    print("Packet Mismatch (path):")
                    raise self.conn.TimeoutException
                return
            except self.conn.TimeoutException as e:
                pass

        # necesitamos sincronizar las respuestas, lo hacemos con GetAll()
        packet = self._makeS2Packet(65)
        while(True):
            self.conn.write(packet)
            try:
                self.conn.read(11) # estos bytes quedaron sin ser recibidos
                self.conn.read(self.PACKET_LENGTH)
                break
            except self.conn.TimeoutException as e:
                pass

        # solicitamos el estado de los sensores
        self._sendS2Command(packet, 0)

    def _getS2SensorsResponse(self)->HS2Sensors:
        """Obtiene estado de los principales sensores del S2."""
        return HS2Sensors(self._getUInt8Response() , self._getUInt8Response() ,
                          self._getUInt16Response(), self._getUInt16Response(),
                          self._getUInt16Response(),
                          self._getUInt8Response() , self._getUInt8Response() ,
                          self._getUInt8Response())

    def _getLineResponse(self, maxChars:int)->str:
        """Obtiene una respuesta del S2 como un string ascii."""
        return self.conn.readLine(maxChars)

    def _getUInt8Response(self)->int:
        """Obtiene una respuesta del S2 como un entero de 8 bits sin signo."""
        return self.conn.readUInt8()

    def _getUInt16Response(self)->int:
        """Obtiene una respuesta del S2 como un entero de 16 bits sin signo."""
        return self.conn.readUInt16()

    def _getUInt32Response(self)->int:
        """Obtiene una respuesta del S2 como un entero de 32 bits sin signo."""
        return self.conn.readUInt32()

    def _getInt32Response(self)->int:
        """Obtiene una respuesta del S2 como un entero de 32 bits con signo."""
        return self.conn.readInt32()

    def _getBytesResponse(self, nbytes:int)->bytearray:
        """Obtiene una respuesta del S2 como un conjunto de bytes."""
        return self.conn.read(nbytes)

    def _lock(self)->None:
        """Obtiene acceso exclusivo al S2."""
        self.mylock.acquire()

    def _unlock(self)->None:
        """Libera el acceso exclusivo al S2."""
        self.mylock.release()
