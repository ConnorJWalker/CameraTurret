import cv2
import math

class Detector:
    def __init__(self):
        self.classifier = cv2.CascadeClassifier("Camera/haarcascade_frontalface_default.xml")

    def detect(self, image):
        greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return self.classifier.detectMultiScale(greyscale)

    def getClosestIndex(self, faces, image):
        closestDistance = -1
        closestIndex = -1
        self.imageCenter = self.getScreenCenter(image)

        for i in range(len(faces)):
            face = faces[i]

            distance = self.getDistanceFromCenter(face)
            if closestDistance == -1 or distance < closestDistance:
                closestDistance = distance
                closestIndex = i

        return closestIndex

    def getScreenCenter(self, image):
        centerX = len(image[0]) / 2
        centerY = len(image) / 2

        return centerX, centerY

    def getFaceCenter(self, face):
        x, y, width, height = face

        centerX = x + width / 2
        centerY = y + height / 2

        return centerX, centerY

    def getDistanceFromCenter(self, face):
        faceCenter = self.getFaceCenter(face)
        distanceX = abs(self.imageCenter[0] - faceCenter[0])
        distanceY = abs(self.imageCenter[1] - faceCenter[1])

        return math.sqrt((distanceX * distanceX) + (distanceY * distanceY))
