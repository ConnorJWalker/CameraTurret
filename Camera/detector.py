import cv2

class Detector:
    def __init__(self):
        self.classifier = cv2.CascadeClassifier("Camera/haarcascade_frontalface_default.xml")

    def detect(self, image):
        greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return self.classifier.detectMultiScale(greyscale)
