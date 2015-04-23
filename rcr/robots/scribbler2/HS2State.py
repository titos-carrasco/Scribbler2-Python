# -*- coding: utf-8 -*-

class HS2State:
    def __init__( self, inPins, outPins ):
        self.inPins = inPins
        self.outPins = outPins

    def __str__( self ):
        return "HS2State(%d, %d)" % ( self.inPins, self.outPins )
