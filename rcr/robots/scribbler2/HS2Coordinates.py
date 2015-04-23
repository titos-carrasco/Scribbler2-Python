# -*- coding: utf-8 -*-

class HS2Coordinates:
    def __init__( self, x, y ):
        self.x = x
        self.y = y

    def __str__( self ):
        return "HS2Coordinates(%d, %d)" % ( self.x, self.y )
