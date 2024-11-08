import numpy as np  # pip install numpy
import cv2  # pip install opencv-python
from scribbler2.S2Fluke2 import S2Fluke2


class App:
    def __init__(self, dev):
        self.robot = S2Fluke2(dev)

    def run(self):
        cv2.namedWindow("Frames", cv2.WINDOW_AUTOSIZE)
        self.robot.setPicSize(self.robot.IMAGE_SMALL)
        for i in range(10):
            image = self.robot.getImage(self.robot.IMAGE_GRAYJPEG_FAST)
            print("Image:", image)
            img = cv2.imdecode(
                np.frombuffer(image.image, np.uint8), cv2.IMREAD_ANYCOLOR
            )
            cv2.imshow("Frames", img)
            k = cv2.waitKey(5)
        cv2.destroyAllWindows()

        self.robot.close()


# ---
app = App("/dev/rfcomm2")
app.run()
