# -*- coding: utf-8 -*-

class HS2Infrared:
    def __init__( self, irLeft, irRight ):
        self.irLeft = irLeft
        self.irRight = irRight

    def __str__( self ):
        return "HS2Infrared(%d, %d)" % (self.irLeft, self.irRight)
