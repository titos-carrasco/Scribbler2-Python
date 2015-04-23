# -*- coding: utf-8 -*-

class HS2Encoders:
    def __init__( self, left, right ):
        self.left = left
        self.right = right

    def __str__( self ):
        return "HS2Encoders(%d, %d)" % ( self.left, self.right )
