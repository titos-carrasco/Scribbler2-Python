# -*- coding: utf-8 -*-

class HS2MotorStats:
    def __init__( self, stat, moveReady ):
        self.stat = stat
        self.moveReady = moveReady

    def __str__( self ):
        return "HS2MotorStats(%d, %d)" % ( self.stat, self.moveReady )
