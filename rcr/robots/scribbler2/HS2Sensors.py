# -*- coding: utf-8 -*-

class HS2Sensors:
    def __init__( self, irLeft, irRight,
                        lightLeft, lightCenter, lightRight,
                        lineLeft, lineRight, stall ):
        self.irLeft = irLeft
        self.irRight = irRight
        self.lightLeft = lightLeft
        self.lightCenter = lightCenter
        self.lightRight = lightRight
        self.lineLeft = lineLeft
        self.lineRight = lineRight
        self.stall = stall

    def __str__( self ):
        return "IR( %d, %d ), Light( %d, %d, %d ), Line( %d, %d ), Stall( %d )" % \
                (self.irLeft, self.irRight,
                 self.lightLeft, self.lightCenter, self.lightRight,
                 self.lineLeft, self.lineRight,
                 self.stall)
