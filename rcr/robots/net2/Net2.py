# -*- coding: utf-8 -*-

"""Acceso a todas las funcionalidades del Scribbler2 (S2) y de la Fluke 2 (F2)."""

from rcr.utils.SerialNet import SerialNet
from rcr.utils import Utils

from rcr.robots.scribbler2.Scribbler2 import Scribbler2


class Net2( Scribbler2 ):
    """Clase central de interaccion ccon el modulo de red para el S2."""

    def __init__( self, host, port, timeout=500 ):
        """
        Corresponde al constructor de la clase.

        @type host: string
        @param host: host a conectar
        @type port: integer
        @param port: port a conectar en el host
        @type timeout: integer
        @param timeout: timeout para cada comando
        """
        super( Net2, self ).__init__()
        self.conn = SerialNet( host=host, port=port, timeout=timeout )
