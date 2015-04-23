# -*- coding: utf-8 -*-

import time

def pause( ms ):
    time.sleep( ms/1000.0 )

def bytesToHex( b ):
    return "".join("%02x" % d for d in b)

def debug( msg ):
    if( type( msg ) is bytearray ):
        msg = bytesToHex( msg )
    print msg
