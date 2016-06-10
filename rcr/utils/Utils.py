# -*- coding: utf-8 -*-

""" Funciones varias

"""

import time

def pause( ms ):
    """ Pausa la ejecución del programa por un tiempo específico

    Args:
        ms (int): milisegundos a pausar

    """
    time.sleep( ms/1000.0 )

def bytesToHex( b ):
    """ Convierte bytes a su representación hexadecimal

    Args:
        b (bytes, bytearray o compatibles): los bytes a convertir

    Returns:
        str: representación hexadecimal de los bytes

    """
    return ''.join('%02x' % d for d in b)

def debug( msg ):
    """ Despliega en consola un mensaje

    Args:
        msg (str): el mensaje a desplegar

    """
    if( type( msg ) is bytearray ):
        msg = bytesToHex( msg )
    print( msg )
