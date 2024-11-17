import time
from threading import Thread
import pygame  # pip install pygame
import gi  # pip install pygobject

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from scribbler2.Fluke2 import Robot  # conexion via bluethoot a la Fluke2


class TestJoystick:

    def __init__(self):
        """Construye la GUI desde el archivo glade."""
        self.builder = Gtk.Builder()
        self.builder.add_from_file("Resources/Scribbler2.glade")
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("MainWindow")
        self.window.show_all()
        self.rob = None
        self.move_buttons = self.builder.get_object("MoveButtons")
        self.speed = self.builder.get_object("Speed")
        self.speed.props.adjustment = self.builder.get_object("SpeedAdjustment")
        self.speed_value = 0
        self.port = self.builder.get_object("Port")
        self.connect = self.builder.get_object("Connect")
        self.status_bar = self.builder.get_object("StatusBar")
        self.sb_context_id = self.status_bar.get_context_id("MainMessages")
        self.info = self.builder.get_object("Info")
        self.ir_left = self.builder.get_object("IRLeft")
        self.ir_right = self.builder.get_object("IRRight")
        self.light_left = self.builder.get_object("LightLeft")
        self.light_center = self.builder.get_object("LightCenter")
        self.light_right = self.builder.get_object("LightRight")
        self.line_left = self.builder.get_object("LineLeft")
        self.line_right = self.builder.get_object("LineRight")
        self.stall = self.builder.get_object("Stall")
        self.tjoystick = None
        self.tsensors = None

        self.time_sensors = time.time()
        self.sensors = None

    def onDeleteWindow(self, *args):
        self.onQuit(*args)

    def onQuit(self, *_args):
        self.connect.set_active(False)
        Gtk.main_quit()

    def onConnect(self, *_args):
        if self.connect.get_active():
            self._SbSetMessage("Conectando...")
            try:
                self.rob = Robot(port=self.port.get_text())
            except Exception:  # pylint: disable=broad-except
                self.connect.set_active(False)
                self._SbSetMessage("Error al conectar con el Scribbler2")
                return
            self._StoreSensors(self.rob.getAllSensors())
            self.move_buttons.set_sensitive(True)
            self.speed.set_sensitive(True)
            self.port.set_sensitive(False)
            self._SbSetMessage(
                f"Conectado a {self.port.get_text()} - Mi nombre es '{self.rob.getName()}'"
            )
            self.info.set_label(self.rob.getInfo())
            self.connect.set_label("Desconectar")

            # Inicia el hilo de los sensores
            self.tsensors = Thread(target=self._Sensors, args=())
            self.tsensors.start()

            # Inicia el hilo del joystick
            pygame.init()
            if pygame.joystick.get_count() > 0:
                self.tjoystick = Thread(target=self._Joystick, args=())
                self.tjoystick.start()
        else:
            if self.rob is not None:
                self.rob.close()
                self.rob = None
                self.move_buttons.set_sensitive(False)
                self.speed.set_sensitive(False)
                self.port.set_sensitive(True)
                self.info.set_label("")
                self._SbSetMessage("Desconectado")
                self.connect.set_label("Conectar")

                # Detiene el hilo de sensors
                if self.tsensors is not None:
                    self.tsensors.join()
                    self.tsensors = None

                # Detiene  el hilo del joystick
                if self.tjoystick is not None:
                    self.tjoystick.join()
                    self.tjoystick = None
                pygame.quit()
        return

    def onSpeedChanged(self, *_args):
        self.speed_value = int(self.speed.props.adjustment.get_value())

    def onUp(self, *_args):
        self._StoreSensors(self.rob.setMotors(self.speed_value, self.speed_value))

    def onUpLeft(self, *_args):
        self._StoreSensors(self.rob.setMotors(self.speed_value / 4, self.speed_value))

    def onUpRight(self, *_args):
        self._StoreSensors(self.rob.setMotors(self.speed_value, self.speed_value / 4))

    def onDown(self, *_args):
        self._StoreSensors(self.rob.setMotors(-self.speed_value, -self.speed_value))

    def onDownLeft(self, *_args):
        self._StoreSensors(self.rob.setMotors(-self.speed_value / 4, -self.speed_value))

    def onDownRight(self, *_args):
        self._StoreSensors(self.rob.setMotors(-self.speed_value, -self.speed_value / 4))

    def onLeft(self, *_args):
        self._StoreSensors(self.rob.setMotors(-self.speed_value, self.speed_value))

    def onRight(self, *_args):
        self._StoreSensors(self.rob.setMotors(self.speed_value, -self.speed_value))

    def onStop(self, *_args):
        self._StoreSensors(self.rob.setMotorsOff())

    def _SbSetMessage(self, msg=None):
        self.status_bar.pop(self.sb_context_id)
        if msg is not None:
            self.status_bar.push(self.sb_context_id, msg)

    def _StoreSensors(self, sensors):
        self.time_sensors = time.time()
        self.sensors = sensors

    def _Sensors(self, *_args):
        """Hilo que procesa el despliegue de los sensores."""
        while self.rob is not None:
            try:
                t = time.time()
                if (t - self.time_sensors) > 1:
                    self._StoreSensors(self.rob.getAllSensors())
                self.ir_left.set_label(str(self.sensors.ir_left))
                self.ir_right.set_label(str(self.sensors.ir_right))
                self.light_left.set_label(str(self.sensors.light_left))
                self.light_center.set_label(str(self.sensors.light_center))
                self.light_right.set_label(str(self.sensors.light_right))
                self.line_left.set_label(str(self.sensors.line_left))
                self.line_right.set_label(str(self.sensors.line_right))
                self.stall.set_label(str(self.sensors.stall))
                time.sleep(1)
            except Exception as e:  # pylint: disable=broad-except
                print(e)
                break

    def _Joystick(self, *_args):
        """Hilo que procesa los eventos del joystick."""
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        axes = [0] * joystick.get_numaxes()
        (_x, _y) = (0, 0)

        # procesa mientras el objeto del robot exista
        while self.rob is not None:
            try:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.JOYAXISMOTION and event.joy == 0:
                        axes[event.axis] = int(round(event.value, 0))
                (x, y) = (axes[0], -axes[1])
                if (_x, _y) != (x, y):
                    (_x, _y) = (x, y)
                    if x == 0 and y == 1:
                        self.onUp()
                    elif x == 0 and y == -1:
                        self.onDown()
                    elif x == -1 and y == 1:
                        self.onUpLeft()
                    elif x == 1 and y == 1:
                        self.onUpRight()
                    elif x == -1 and y == -1:
                        self.onDownLeft()
                    elif x == 1 and y == -1:
                        self.onDownRight()
                    elif x == -1 and y == 0:
                        self.onLeft()
                    elif x == 1 and y == 0:
                        self.onRight()
                    else:
                        self.onStop()
                time.sleep(0.1)
            except Exception as e:  # pylint: disable=broad-except
                print(e)
                break


# ---
app = TestJoystick()
Gtk.main()
