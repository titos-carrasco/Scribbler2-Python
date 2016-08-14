# -*- coding: utf-8 -*-

"""Funciones varias de apoyo."""

import time

def pause( ms ):
    """Pausa la ejecucion del programa por un tiempo especifico.

    Args:
        ms (int): milisegundos a pausar

    """
    time.sleep( ms/1000.0 )

def bytesToHex( b ):
    """Convierte bytes a su representacion hexadecimal.

    Args:
        b (bytes, bytearray o compatibles): los bytes a convertir

    Returns:
        str: representacion hexadecimal de los bytes

    """
    return ''.join('%02x' % d for d in b)

def debug( msg ):
    """Despliega en consola un mensaje.

    Args:
        msg (str): el mensaje a desplegar

    """
    if( type( msg ) is bytearray ):
        msg = bytesToHex( msg )
    print( msg )
