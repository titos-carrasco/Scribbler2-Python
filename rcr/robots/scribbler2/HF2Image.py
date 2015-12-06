# -*- coding: utf-8 -*-

class HF2Image:
    def __init__( self, width, height, image ):
        self.width = width
        self.height = height
        self.image = image

    def __str__( self ):
        return "F2Camera(%d, %d, %d)" % ( self.width, self.height, len( self.image ) )
