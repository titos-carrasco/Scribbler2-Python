# -*- coding: utf-8 -*-

class HS2Lights:
    def __init__( self, lightLeft, lightCenter , lightRight ):
        self.lightLeft = lightLeft
        self.lightCenter = lightCenter
        self.lightRight = lightRight

    def __str__( self ):
        return "HS2Lights(%d, %d, %d)" % ( self.lightLeft, self.lightCenter, self.lightRight )
