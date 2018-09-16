#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Servidor para ejecutar acciones sobre el S2 desde Snap.

(snapext presenta errores en python3)
"""


from __future__ import division, print_function

import sys
import snapext

#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.robots.fluke2.Fluke2 import Fluke2
from rcr.utils import Utils

s2 = None
handler = snapext.SnapHandler

@handler.route( '/Connect' )
def Connect( port='/dev/rfcomm2', bauds=9600, timeout=500, dtr=None ):
    """Conecta al S2 que se encuentra en la puerta especificada."""
    global s2

    if( s2 != None ):
        try:
            print( 'S2 Connect(): Cerrando conexion anterior ...' )
            s2.close()
            print( 'OK' )
        except:
            pass
    try:
        if( dtr == True ):
            dtr = True
        elif( dtr == False ):
            dtr = False
        else:
            dtr = None
        print( 'S2 Connect(): Estableciendo conexion con el S2 ... ' )
        #s2 = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
        s2 = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        #s2 = Net2( "192.168.145.1", 1500, 500 )
        print( 'OK' )
    except Exception as e:
        print( 'S2 Connect(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()

@handler.route( '/Close' )
def Close():
    """Finaliza la conexion con el S2."""
    global s2
    try:
        print( 'S2 Close(): Cerrando conexion ...' )
        s2.close()
        print( 'OK' )
    except Exception as e:
        print( 'S2 Close(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()
        s2 = None

@handler.route( '/GetInfo' )
def GetInfo():
    """Obtiene informacion general del S2."""
    global s2
    try:
        print( 'S2 GetInfo(): Recuperando data ...' )
        info = s2.getS2Inner().getInfo()
        print( info )
        print( 'OK' )
        return info
    except Exception as e:
        print( 'S2 GetInfo(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()

@handler.route( '/SetMotors' )
def SetMotors( left=50, right=50 ):
    """
    Control de los motores del S2.

        - left (int): valor de poder motor izquierdo (-100 a 100, 0 lo detiene)
        - right (int): valor de poder motor derecho (-100 a 100, 0 lo detiene)

    """
    global s2
    try:
        print( 'S2 SetMotors(): Estableciendo motores {left}, {right} ...'.format( left=left, right=right ) )
        sensors = _listSensors( s2.getS2Motors().setMotors( left, right ) )
        print( sensors )
        print( 'OK' )
        return sensors
    except Exception as e:
        print( 'S2 SetMotors(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()

@handler.route( '/GetSensors' )
def GetSensors():
    """Obtiene el valor de los sensores."""
    global s2
    try:
        print( 'S2 GetSensors(): Recuperando sensores ...' )
        sensors = _listSensors( s2.getS2Inner().getAllSensors() )
        print( sensors )
        print( 'OK' )
        return sensors
    except Exception as e:
        print( 'S2 GetSensors(): Exception' )
        print( e )
        return []
    finally:
        sys.stdout.flush()

@handler.route( '/GetName' )
def GetName():
    """Obtiene el nombre de este S2."""
    global s2
    try:
        print( 'S2 GetName(): Recuperando nombre ...' )
        name = s2.getS2Inner().getName()
        print( name )
        print( 'OK' )
        return name
    except Exception as e:
        print( 'S2 GetName(): Exception' )
        print( e )
        return ''
    finally:
        sys.stdout.flush()

@handler.route( '/SetName' )
def SetName( name = 'MyBot' ):
    """Establece un nombre para el S2."""
    global s2
    try:
        print( 'S2 SetName(): Estableciendo nombre "{name}" ...'.format( name=name ) )
        sensors = _listSensors( s2.getS2Inner().setName( name ) )
        print( sensors )
        print( 'OK' )
        return sensors
    except Exception as e:
        print( 'S2 setName(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()

@handler.route( '/GetMic' )
def GetMic():
    """Obtiene valor actual del microfono del S2."""
    global s2
    try:
        print( 'S2 GetMic(): Recuperando valor del microfono ...' )
        mic = s2.getS2Microphone().getMicEnv()
        print( mic )
        print( 'OK' )
        return mic
    except Exception as e:
        print( 'S2 GetMic(): Exception' )
        print( e )
        return 0
    finally:
        sys.stdout.flush()

@handler.route( '/SetLEDs' )
def SetLEDs( left='on', center='on', right='on' ):
    """Establece el estado de los leds del S2."""
    global s2
    try:
        left = 1 if left=='on' else 0
        center = 1 if center=='on' else 0
        right = 1 if right=='on' else 0
        print( 'S2 SetLEDs(): seteando LEDs {left}, {center}, {right} ...'.format( left=left, center=center, right=right ) )
        sensors = _listSensors( s2.getS2LEDs().setAllLed( left, center, right ) )
        print( sensors )
        print( 'OK' )
        return sensors
    except Exception as e:
        print( 'S2 SetLEDs(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()

@handler.route( '/PlayTone' )
def PlayTone( freq=440, duration=500, volume=50 ):
    """
    Genera un sonido en el S2.

        - freq (int): la frecuencia del sonido a reproducir
        - duration (int): duracion del sonido en milisegundos
        - volume (int): volumen del sonido (0 a 100)

    """
    global s2
    try:
        print( 'S2 PlayTone(): Generando sonido {freq}, {duration}, {volume} ...'.format( freq=freq, duration=duration, volume=volume ) )
        speaker = s2.getS2Speaker()
        speaker.setLoud()
        speaker.setVolume( volume )
        sensors = _listSensors( speaker.setSpeaker( duration, freq, 0 ) )
        #speaker.setQuiet()
        print( sensors )
        print( 'OK' )
        return sensors
    except Exception as e:
        print( 'S2 PlayTone(): Exception' )
        print( e )
    finally:
        sys.stdout.flush()

def _listSensors( allSensors ):
    sensors = [0]*8
    sensors[0] = allSensors.irLeft
    sensors[1] = allSensors.irRight
    sensors[2] = allSensors.lightLeft
    sensors[3] = allSensors.lightCenter
    sensors[4] = allSensors.lightRight
    sensors[5] = allSensors.lineLeft
    sensors[6] = allSensors.lineRight
    sensors[7] = allSensors.stall
    return sensors

# main()
while( True ):
    try:
        snapext.main( handler, 1963 )
    except Exception as e:
        print( 'MainLoop Exception' )
        print( e )
        sys.stdout.flush()
