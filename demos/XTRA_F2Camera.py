#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de la camara de la tarjeta F2."""

# cv2 presenta errores en python3

import numpy as np
import cv2

from rcr.robots.fluke2.Fluke2 import Fluke2

def main():
    """Realiza las pruebas de la camara de la tarjeta de la F2.

    Las pruebas utilizan las librerias numpy y opencv, y consideran:
        robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
        f2Camera = robot.getF2Camera()

        f2Camera.setPicSize)
        f2Camera.getImage()

    """
    robot = Fluke2( port="/dev/rfcomm2", bauds=9600, timeout=500 )
    f2Camera = robot.getF2Camera()

    cv2.namedWindow( 'Frames', cv2.WINDOW_AUTOSIZE )
    f2Camera.setPicSize( f2Camera.IMAGE_SMALL )
    for i in range(10):
        image = f2Camera.getImage( f2Camera.IMAGE_GRAYJPEG_FAST )
        print( "Image:" + str( image ) )
        img = cv2.imdecode( np.frombuffer( image.image, np.uint8 ), cv2.IMREAD_ANYCOLOR )
        cv2.imshow( 'Frames', img )
        k = cv2.waitKey(5)
    cv2.destroyAllWindows()
    robot.close()


if( __name__ == "__main__" ):
    main()
