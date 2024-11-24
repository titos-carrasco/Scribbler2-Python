import rtmidi  # pip install python-rtmidi

# from scribbler2.S2 import Robot  # conexion via cable serial
from scribbler2.Fluke2 import Robot  # conexion via bluethoot a la Fluke2


class App:
    def __init__(self, dev):
        self.robot = Robot(dev)

    def run(self):
        print("Creando puerta MIDI")
        midi_in = rtmidi.MidiIn()
        midi_in.open_virtual_port("S2 Control Port")

        print("Conecte la puerta del Controlador Midi a la puerta virtual creada")
        while True:
            while True:
                data = midi_in.get_message()
                if data is None:
                    continue
                msg = data[0]
                event = msg[0] & 0xF0

                # note on event
                if event == 0x90:
                    channel = msg[0] & 0x0F
                    note = msg[1]
                    velocity = msg[2]
                    print(channel, note, velocity)

                    # middle C = 60
                    if note == 60:
                        self.robot.setMotors(100, -100)
                    elif note == 61:
                        self.robot.setMotors(-100, 100)
                    elif note == 62:
                        self.robot.setMotors(100, 100)
                    elif note == 63:
                        self.robot.setMotors(-100, -100)
                    elif note == 64:
                        self.robot.setMotorsOff()
        midi_in.close()
        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
