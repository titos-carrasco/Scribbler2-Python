#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de la camara de la tarjeta F2."""

import numpy as np
import cv2

from scribbler2.S2Fluke2 import S2Fluke2

def main():
    """Realiza las pruebas de la camara de la tarjeta de la F2."""

    robot = S2Fluke2( "/dev/rfcomm2" )

    cv2.namedWindow( 'Frames', cv2.WINDOW_AUTOSIZE )
    robot.setPicSize( robot.IMAGE_SMALL )
    for i in range(10):
        image = robot.getImage( robot.IMAGE_GRAYJPEG_FAST )
        print( "Image:", image )
        img = cv2.imdecode( np.frombuffer( image.image, np.uint8 ), cv2.IMREAD_ANYCOLOR )
        cv2.imshow( 'Frames', img )
        k = cv2.waitKey(5)
    cv2.destroyAllWindows()

    robot.close()


if( __name__ == "__main__" ):
    main()
