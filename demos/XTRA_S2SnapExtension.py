#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Extensión para trabajar con el S2 en SNAP y SCRATCH."""

from __future__ import division, print_function

import sys
from blockext import *

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

s2 = None

@command( 'S2 connect to %s', blocking=True )
def connect( port='rfcomm2' ):
    """Conecta al S2 que se encuentra en la puerta especificada."""
    global s2
    if( s2 != None ):
        try:
            print( 'S2 connect(): Cerrando conexion anterior' )
            s2.close()
        except:
            pass
    try:
        print( 'S2 connect(): Estableciendo conexion con el S2 ... ', end='' )
        s2 = Scribbler2( '/dev/' + port, 9600, 500 )
        print( 'OK' )
    except Exception as e:
        print( 'Exception' )
        print( e )
    finally:
        sys.stdout.flush()

@command( 'S2 close', blocking=True )
def close():
    """Finaliza la conexion con el S2."""
    global s2
    try:
        print( 'S2 close(): Cerrando conexion' )
        s2.close()
    except Exception as e:
        print( 'S2 close(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()
        s2 = None

@reporter( 'S2 info' )
def getInfo():
    """Obtiene informacion general del S2."""
    global s2
    try:
        print( 'S2 getInfo(): Recuperando data' )
        return s2.getS2Inner().getInfo()
    except Exception as e:
        print( 'S2 getInfo(): Exception' )
        print( e )
        return ''
    finally:
        sys.stdout.flush()

@reporter( 'S2 sensors' )
def getAllSensors():
    """
    Obtiene el valor de varios sensores del S2 como una lista.

        - [0] sensor IR izquierdo
        - [1] sensor IR derecho
        - [2] sensor de luz izquierdo
        - [3] sensor de luz central
        - [4] sensor de luz derecho
        - [5] sensor de linea izquierdo
        - [6] sensor de linea derecho
        - [7] sensor de atasco de motores

    """
    global s2
    try:
        print( 'S2 getAllSensors(): Recuperando sensores' )
        sensors = []
        s2Sensors = s2.getS2Inner().getAllSensors()
        sensors.append( s2Sensors.irLeft )
        sensors.append( s2Sensors.irRight )
        sensors.append( s2Sensors.lightLeft )
        sensors.append( s2Sensors.lightCenter )
        sensors.append( s2Sensors.lightRight )
        sensors.append( s2Sensors.lineLeft )
        sensors.append( s2Sensors.lineRight )
        sensors.append( s2Sensors.stall )
        return sensors
    except Exception as e:
        print( 'S2 getAllSensors(): Exception' )
        print( e )
        return []
    finally:
        sys.stdout.flush()

@reporter( 'S2 name' )
def getName():
    """Obtiene el nombre de este S2."""
    global s2
    try:
        print( 'S2 getName(): Recuperando nombre' )
        return s2.getS2Inner().getName()
    except Exception as e:
        print( 'S2 getName(): Exception' )
        print( e )
        return ''
    finally:
        sys.stdout.flush()

@command( 'S2 setName %s', blocking=True )
def setName( name = 'myName' ):
    """Establece un nombre para el S2."""
    global s2
    try:
        print( 'S2 setName(): Estableciendo nombre "{name}"'.format( name=name ) )
        s2.getS2Inner().setName( name )
    except Exception as e:
        print( 'S2 setName(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()

menu( 'OnOff', [ 'on', 'off' ] )
@command( 'S2 setLEDs left: %m.OnOff center: %m.OnOff and right: %m.OnOff', blocking=True )
def setLEDs( left='on', center='on', right='on' ):
    """Establece el estado de los leds del S2."""
    global s2
    try:
        left = 1 if left=='on' else 0
        center = 1 if center=='on' else 0
        right = 1 if right=='on' else 0
        print( 'S2 setLEDs(): seteando LEDs {left}, {center}, {right}'.format( left=left, center=center, right=right ) )
        s2.getS2LEDs().setAllLed( left, center, right )
    except Exception as e:
        print( 'S2 setLEDs(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()

@command( 'S2 setMotors left: %n right: %n', blocking=True )
def setMotors( left=50, right=50 ):
    """
    Control de los motores del S2.

        - left (int): valor de poder motor izquierdo (-100 a 100, 0 lo detiene)
        - right (int): valor de poder motor derecho (-100 a 100, 0 lo detiene)

    """
    global s2
    try:
        print( 'S2 setMotors(): Estableciendo motores {left}, {right}'.format( left=left, right=right ) )
        s2.getS2Motors().setMotors( left, right )
    except Exception as e:
        print( 'S2 setMotors(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()

@reporter( 'S2 get mic value' )
def getMic():
    """Obtiene valor actual del microfono del S2."""
    global s2
    try:
        print( 'S2 getMic(): Recuperando valor del microfono' )
        return s2.getS2Microphone().getMicEnv()
    except Exception as e:
        print( 'S2 getMic(): Exception' )
        print( e )
        return 0
    finally:
        sys.stdout.flush()

@command( 'S2 makeSound freq: %n duration: %n volume: %n', blocking=True )
def setSpeaker( freq=440, duration=500, volume=50 ):
    """
    Genera un sonido en el S2.

        - freq (int): la frecuencia del sonido a reproducir
        - duration (int): duracion del sonido en milisegundos
        - volume (int): volumen del sonido (0 a 100)

    """
    global s2
    try:
        print( 'S2 makeSound(): Generando sonido {freq}, {duration}, {volume}'.format( freq=freq, duration=duration, volume=volume ) )
        speaker = s2.getS2Speaker()
        speaker.setLoud()
        speaker.setVolume( volume )
        speaker.setSpeaker( duration, freq, 0 )
        speaker.setQuiet()
    except Exception as e:
        print( 'S2 makeSound(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()

#@reporter( 'S2 take picture' )
#def takePicture():
#    """Captura una imagen desde la camara de la F2.
#
#    Returns:
#        bytearray: bitmap de la imagen en formato JPEG
#
#    """
#    global s2
#    try:
#        print( 'S2 takePicture(): Capturando imagen' )
#        cam = s2.getF2Camera()
#        cam.setPicSize( cam.IMAGE_SMALL )
#        return cam.getImage( cam.IMAGE_GRAYJPEG_FAST )
#    except Exception as e:
#        print( e )
#        return bytearray()

while( True ):
    try:
        blockext.run( 'Parallax S2 robot and Fluke2 card', 'S2Robot', 1963 )
    except Exception as e:
        print( 'MainLoop Exception' )
        print( e )
        sys.stdout.flush()

