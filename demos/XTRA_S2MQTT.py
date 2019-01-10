#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test del S2 via MQTT.

Requiere de paho (pip install paho-mqtt)
"""
from __future__ import print_function

import paho.mqtt.client as paho
#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.robots.fluke2.Fluke2 import Fluke2
from rcr.utils import Utils
import json
import time
import unicodedata
try:
    import Queue as queue
except:
    import queue

MQTT_SERVER = 'test.mosquitto.org'
MQTT_PORT = 1883
S2_TOPIC  = 'rcr/S2'

messages = queue.Queue( 1 )

def mqtt_on_connect( client, userdata, flag, rc ):
    """Invocada al conectar a servidor MQTT."""
    global S2_TOPIC, MQTT_SERVER, MQTT_PORT

    client.subscribe( S2_TOPIC )
    print( "[S2] Esperando en %s:%s - %s" % ( MQTT_SERVER, MQTT_PORT, S2_TOPIC ) )

def mqtt_on_message( client, userdata, message ):
    """Invocada al recibir mensaje MQTT en algun topico suscrito."""
    global messages

    # si no se ha procesado el ultimo mensaje lo eliminamos
    try:
        messages.get_nowait()
    except queue.Empty:
        pass

    # agregamos el mensaje
    try:
        messages.put_nowait( message )
    except queue.Full:
        pass


def main():
    """Realiza pruebas del S2 recibiendo comandos via MQTT."""
    global mqtt_client, MQTT_SERVER, MQTT_PORT, messages

    print( "Comandos:" )
    print( "  name" )
    print( "  left"  )
    print( "  right" )
    print( "  forward" )
    print( "  backwward" )
    print( "  stop" )
    print( "  exit" )
    print( "---" )

    mqtt_client = paho.Client()
    mqtt_client.on_connect = mqtt_on_connect
    mqtt_client.on_message = mqtt_on_message
    mqtt_client.connect( MQTT_SERVER, MQTT_PORT )
    mqtt_client.loop_start()
    s2 = None
    abort = False
    try:
        #robot = Scribbler2( port="/dev/ttyUSB1", bauds=38400, timeout=500, dtr=False )
        robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        #robot = Net2( "192.168.145.1", 1500, 500 )
    except Exception as e:
        abort = True
    while( not abort ):
        message = messages.get()
        payload = message.payload.decode( 'utf-8' )
        print( "[S2] Mensaje recibido:", payload )

        words = payload.split()
        cmd = words[0]
        if( cmd == 'exit' ):
            abort = True
        elif( cmd == 'name' ):
            print( robot.getS2Inner().getName() )
        elif( cmd == 'left' ):
            robot.getS2Motors().setMotors( -100, 100 )
        elif( cmd == 'right' ):
            robot.getS2Motors().setMotors( 100, -100 )
        elif( cmd == 'forward' ):
            robot.getS2Motors().setMotors( 100, 100 )
        elif( cmd == 'backward' ):
            robot.getS2Motors().setMotors( -100, -100 )
        elif( cmd == 'stop' ):
            robot.getS2Motors().setMotors( 0, 0 )

    mqtt_client.loop_stop()
    robot.close()

if( __name__ == "__main__" ):
    main()
