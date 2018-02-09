# -*- coding: utf-8 -*-

"""Funciones varias de apoyo."""

import time

def pause( ms ):
    """
    Pausa la ejecucion del programa por un tiempo especifico.

    @type ms: integer
    @param ms: milisegundos de pausa
    """
    time.sleep( ms/1000.0 )

def bytesToHex( b ):
    """
    Convierte bytes a su representacion hexadecimal.

    @type b: byte, bytearray o compatible
    @param b: los bytes a convertir a hexadecimal
    @rtype: string
    @return: representacion hexadecimal de los bytes
    """
    return ''.join('%02x' % d for d in b)

def debug( msg ):
    """
    Despliega en consola un mensaje.

    @type msg: string
    @param msg: el mensaje a desplegar
    """
    if( type( msg ) is bytearray ):
        msg = bytesToHex( msg )
    print( msg )
