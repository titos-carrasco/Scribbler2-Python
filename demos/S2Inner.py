from scribbler2.S2Fluke2 import S2Fluke2

class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        print( "getInfo      : ", self.robot.getInfo() )
        print( "getAllSensors: ", self.robot.getAllSensors() )
        print( "setPass      : ", self.robot.setPass( "1234567898765432" ) )
        print( "getPass      : ", self.robot.getPass() )
        print( "setPass      : ", self.robot.setPass( "ABCDEFGHIJKLMNOP" ) )
        print( "getPass      : ", self.robot.getPass() )
        print( "setName      : ", self.robot.setName( "NAME1234" ) )
        print( "getName      : ", self.robot.getName() )
        print( "setName      : ", self.robot.setName( "TitosBot" ) )
        print( "getName      : ", self.robot.getName() )
        print( "getState     : ", self.robot.getState() )
        print( "setData      : ", self.robot.setData( bytes( [ 8, 7, 6, 5, 4, 3, 2, 1 ] ) ) )
        print( "getData      : ", bytes.hex( self.robot.getData() ) )
        print( "setSingleData: ", self.robot.setSingleData( 4, 255 ) )
        print( "getData      : ", bytes.hex( self.robot.getData() ) )
        print( "setData      : ", self.robot.setData( bytes( [ 1, 2, 3, 4, 5, 6, 7, 8 ] ) ) )
        print( "getData      : ", bytes.hex( self.robot.getData() ) )

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
