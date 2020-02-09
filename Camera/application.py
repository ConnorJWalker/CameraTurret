import cv2
import detector

class Application:
    def __init__(self, shouldRender):
        self.camera = cv2.VideoCapture(0)
        self.shouldRender = shouldRender
        self.detector = detector.Detector()

    def start(self):
        while True:
            success, frame = self.camera.read()

            if success:
                faces = self.detector.detect(frame)
                if self.shouldRender:
                    self.render(faces, frame)
            else:
                print("Couldn't capture image")

            if cv2.waitKey(1) & 0xFF == ord(u"\u0020"):
                break

    def render(self, faces, frame):
        closest = self.detector.getClosestIndex(faces, frame)

        for i in range(len(faces)):
            x, y, w, h = faces[i]
            print((closest, i))
            colour = (0, 0, 255) if i == closest else (255, 0, 0)
            cv2.rectangle(frame, (x, y), (x + w, y + h), colour)

        cv2.imshow("Detected Faces", frame)
