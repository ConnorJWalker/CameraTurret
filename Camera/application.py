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
                self.render(faces, frame)
            else:
                # print error
                print("Couldn't capture image")

            if cv2.waitKey(1) & 0xFF == ord(u"\u0020"):
                break

    def render(slef, faces, frame):
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0))

        cv2.imshow("Detected Faces", frame)
