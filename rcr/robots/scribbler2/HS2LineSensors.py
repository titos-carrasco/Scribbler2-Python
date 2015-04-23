# -*- coding: utf-8 -*-

class HS2LineSensors:
    def __init__( self, lineLeft, lineRight ):
        self.lineLeft = lineLeft
        self.lineRight = lineRight

    def __str__( self ):
        return "HS2LineSensors(%d, %d)" % ( self.lineLeft, self.lineRight )
