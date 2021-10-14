# -*- coding: utf-8 -*-

"""Acceso a todas las funcionalidades del Scribbler2 (S2) via cable serial."""

import threading
import time

from scribbler2.robot.Scribbler2 import Scribbler2
from scribbler2.Serial import Serial

class S2Serial(Scribbler2):
    """Clase para interactuar con un Scribbler2 via cable serial."""

    def __init__(self, port:str, bauds:int=38400,
                       timeout:int=3500, dtr:bool=False)->None:
        """Inicializa el objeto y lo conecta al S2."""
        conn = Serial(port, bauds, timeout)
        if(not dtr is None):
            conn.setDTR(dtr)
        time.sleep(2.0)
        conn.ignoreInput(100)

        super(S2Serial, self).__init__(conn)
