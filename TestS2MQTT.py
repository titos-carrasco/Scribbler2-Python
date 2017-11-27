#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test del S2 via MQTT"""

import paho.mqtt.client as paho
from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils
import json
import time
import Queue

MQTT_SERVER = 'test.mosquitto.org'
S2_TOPIC  = 'rcr/S2'

messages = Queue.Queue( 1 )

def mqtt_on_message( client, userdata, message ):
    global messages, Queue

    # si no se ha procesado el ultimo mensaje lo eliminamos
    try:
        messages.get_nowait()
    except Queue.Empty:
        pass

    # agregamos el mensaje
    try:
        messages.put_nowait( message )
    except Queue.Full:
            pass

def mqtt_on_connect( client, arg1, arg2, arg3 ):
    global S2_TOPIC, MQTT_SERVER

    client.subscribe( S2_TOPIC )
    print( "[S2] Esperando en %s - %s" % ( MQTT_SERVER, S2_TOPIC ) )

def main():
    """Realiza pruebas del S2 recibiendo comandos via MQTT"""
    global mqtt_client, MQTT_SERVER, messages, Queue

    mqtt_client = paho.Client()
    mqtt_client.on_connect = mqtt_on_connect
    mqtt_client.on_message = mqtt_on_message
    mqtt_client.connect( MQTT_SERVER, 1883 )
    mqtt_client.loop_start()
    s2 = None
    abort = False
    try:
        s2 = Scribbler2( "/dev/rfcomm2", 9600, 500 )
    except Exception as e:
        print( e )
        abort = True
    while( not abort ):
        message = messages.get()
        print( "[S2] Mensaje recibido:", message.payload )

        words = message.payload.split()
        cmd = words[0]
        if( cmd == 'exit' ):
            abort = True
        elif( cmd == 'name' ):
            print( s2.s2Inner.getName() )
        else:
            delay = 0
            try:
                delay = float( words[1] )
            except Exception as e:
                print( "[S2]", e )
                continue
            if( delay <= 0 ):
                continue
            elif( cmd == 'left' ):
                s2.getS2Motors().setMotors( -100, 100 )
                time.sleep( delay )
                s2.getS2Motors().setMotors( 0, 0 )
            elif( cmd == 'right' ):
                s2.getS2Motors().setMotors( 100, -100 )
                time.sleep( delay )
                s2.getS2Motors().setMotors( 0, 0 )
            elif( cmd == 'forward' ):
                s2.getS2Motors().setMotors( 100, 100 )
                time.sleep( delay )
                s2.getS2Motors().setMotors( 0, 0 )
            elif( cmd == 'backward' ):
                s2.getS2Motors().setMotors( -100, -100 )
                time.sleep( delay )
                s2.getS2Motors().setMotors( 0, 0 )

    mqtt_client.loop_stop()

if( __name__ == "__main__" ):
    main()
