#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Demo de control del S2 via josystick e interfaz grafica."""

from __future__ import print_function

import gi
gi.require_version( 'Gtk', '3.0' )
from gi.repository import Gtk
from threading import Thread
import pygame
import time

#from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.robots.fluke2.Fluke2 import Fluke2

class TestJoystick:
    """Aplicacion para controlar el S2 via interfaz grafica y joystick."""

    def __init__(self):
        """Construye la GUI desde el archivo glade."""
        self.builder = Gtk.Builder()
        self.builder.add_from_file("Resources/Scribbler2.glade")
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("MainWindow")
        self.window.show_all()
        self.rob = None
        self.MoveButtons = self.builder.get_object("MoveButtons")
        self.Speed = self.builder.get_object("Speed")
        self.Speed.props.adjustment=self.builder.get_object("SpeedAdjustment")
        self.SpeedValue = 0
        self.Port = self.builder.get_object("Port")
        self.Connect = self.builder.get_object("Connect")
        self.StatusBar = self.builder.get_object("StatusBar")
        self.SbContextId = self.StatusBar.get_context_id("MainMessages")
        self.Info = self.builder.get_object("Info")
        self.IRLeft = self.builder.get_object("IRLeft")
        self.IRRight = self.builder.get_object("IRRight")
        self.LightLeft = self.builder.get_object("LightLeft")
        self.LightCenter = self.builder.get_object("LightCenter")
        self.LightRight = self.builder.get_object("LightRight")
        self.LineLeft = self.builder.get_object("LineLeft")
        self.LineRight = self.builder.get_object("LineRight")
        self.Stall = self.builder.get_object("Stall")
        self.TJoystick = None
        self.TSensors = None

    def OnDeleteWindow(self, *args):
        """Procesa el evento de cerrar ventana - Delete Window."""
        self.OnQuit(*args)

    def OnQuit(self, *args):
        """Procesa el evento de salir - Quit."""
        self.Connect.set_active(False)
        Gtk.main_quit()

    def OnConnect(self, *args):
        """Procesa el evento OnConnect del boton On/Off tipo switch."""
        if(self.Connect.get_active()):
            self._SbSetMessage("Conectando...")
            try:
                #self.rob = Scribbler2( port=self.Port.get_text(), bauds=38400, timeout=500, dtr=False )
                self.rob = Fluke2( port=self.Port.get_text(), bauds=9600, timeout=500 )
               #self.rob = Net2( self.Port.get_text(), 1500, 500 )
            except Exception as e:
                self.Connect.set_active(False)
                self._SbSetMessage("Error al conectar con el Scribbler2")
                return
            self._StoreSensors( self.rob.getS2Inner().getAllSensors() )
            self.MoveButtons.set_sensitive(True)
            self.Speed.set_sensitive(True)
            self.Port.set_sensitive(False)
            self._SbSetMessage("Conectado a %s - Mi nombre es '%s'" % (self.Port.get_text(), self.rob.getS2Inner().getName()))
            self.Info.set_label(self.rob.getS2Inner().getInfo())
            self.Connect.set_label("Desconectar")

            # Inicia el hilo de los sensores
            self.TSensors = Thread(target=self._Sensors, args=())
            self.TSensors.start()

            # Inicia el hilo del joystick
            pygame.init()
            if(pygame.joystick.get_count()>0):
                self.TJoystick = Thread(target=self._Joystick, args=())
                self.TJoystick.start()
        else:
            if(self.rob!=None):
                self.rob.close()
                self.rob = None
                self.MoveButtons.set_sensitive(False)
                self.Speed.set_sensitive(False)
                self.Port.set_sensitive(True)
                self.Info.set_label("")
                self._SbSetMessage("Desconectado")
                self.Connect.set_label("Conectar")

                # Detiene el hilo de sensors
                if(self.TSensors!=None):
                    self.TSensors.join()
                    self.TSensors = None

                # Detiene  el hilo del joystick
                if(self.TJoystick!=None):
                    self.TJoystick.join()
                    self.TJoystick = None
                pygame.quit()
        return

    def OnSpeedChanged(self, *args):
        """Procesa el evento de cambio de velocidad - SpeedChange."""
        self.SpeedValue = int(self.Speed.props.adjustment.get_value())

    def OnUp(self, *args):
        """Procesa el evento de avanzar - Up."""
        self._StoreSensors( self.rob.getS2Motors().setMotors(self.SpeedValue, self.SpeedValue) )

    def OnUpLeft(self, *args):
        """Procesa el evento avanzar izquierda - UpLeft."""
        self._StoreSensors( self.rob.getS2Motors().setMotors(self.SpeedValue/4, self.SpeedValue) )

    def OnUpRight(self, *args):
        """Procesa el evento de avanzar derecha - UpRight."""
        self._StoreSensors( self.rob.getS2Motors().setMotors(self.SpeedValue, self.SpeedValue/4) )

    def OnDown(self, *args):
        """Procesa el evento de retroceder - Down."""
        self._StoreSensors( self.rob.getS2Motors().setMotors(-self.SpeedValue, -self.SpeedValue) )

    def OnDownLeft(self, *args):
        """Procesa el evento de retroceder izquierda - DownLeft."""
        self._StoreSensors( self.rob.getS2Motors().setMotors(-self.SpeedValue/4, -self.SpeedValue) )

    def OnDownRight(self, *args):
        """Procesa el evento de retroceder derecha - DownRight."""
        self._StoreSensors( self.rob.getS2Motors().setMotors(-self.SpeedValue, -self.SpeedValue/4) )

    def OnLeft(self, *args):
        """Procesa el evento mover izquierda - Left."""
        self._StoreSensors( self.rob.getS2Motors().setMotors(-self.SpeedValue, self.SpeedValue) )

    def OnRight(self, *args):
        """Procesa el evento de mover derecha - Right."""
        self._StoreSensors( self.rob.getS2Motors().setMotors(self.SpeedValue, -self.SpeedValue) )

    def OnStop(self, *args):
        """Procesa el evento de detener - Stop."""
        self._StoreSensors( self.rob.getS2Motors().setMotorsOff() )

    def _SbSetMessage(self, msg=None):
        """Coloca un mensaje en la barra de estado."""
        self.StatusBar.pop(self.SbContextId)
        if(msg!=None):
            self.StatusBar.push(self.SbContextId, msg)

    def _StoreSensors(self, sensors):
        """Almacena el estado de los sensores."""
        self.time_sensors = time.time()
        self.sensors = sensors

    def _Sensors(self, *args):
        """Hilo que procesa el despliegue de los sensores."""
        while(self.rob!=None):
            try:
                t = time.time()
                if((t-self.time_sensors)>1):
                    self._StoreSensors( self.rob.getS2Inner().getAllSensors() )
                self.IRLeft.set_label( str( self.sensors.irLeft) )
                self.IRRight.set_label( str( self.sensors.irRight) )
                self.LightLeft.set_label( str( self.sensors.lightLeft) )
                self.LightCenter.set_label( str( self.sensors.lightCenter) )
                self.LightRight.set_label( str( self.sensors.lightRight) )
                self.LineLeft.set_label( str( self.sensors.lineLeft ) )
                self.LineRight.set_label( str( self.sensors.lineRight ) )
                self.Stall.set_label( str( self.sensors.stall ) )
                time.sleep(1)
            except Exception as e:
                print( e )
                break

    def _Joystick(self, *args):
        """Hilo que procesa los eventos del joystick."""
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        axes = [0]*joystick.get_numaxes()
        (_x, _y) = (0, 0)

        # procesa mientras el objeto del robot exista
        while(self.rob!=None):
            try:
                events = pygame.event.get()
                for event in events:
                    if(event.type == pygame.JOYAXISMOTION and event.joy == 0):
                        axes[event.axis] = int(round(event.value, 0))
                (x, y) = (axes[0], -axes[1])
                if((_x, _y)!=(x, y)):
                    (_x, _y) = (x, y)
                    if(x==0 and y==1):
                        self.OnUp()
                    elif(x==0 and y==-1):
                        self.OnDown()
                    elif(x==-1 and y==1):
                        self.OnUpLeft()
                    elif(x==1 and y==1):
                        self.OnUpRight()
                    elif(x==-1 and y==-1):
                        self.OnDownLeft()
                    elif(x==1 and y==-1):
                        self.OnDownRight()
                    elif(x==-1 and y==0):
                        self.OnLeft()
                    elif(x==1 and y==0):
                        self.OnRight()
                    else:
                        self.OnStop()
                time.sleep(0.1)
            except:
                break


def main():
    """Demo de control del S2 con interfaz GUI."""
    app = TestJoystick()
    Gtk.main()

if( __name__ == "__main__" ):
    main()
