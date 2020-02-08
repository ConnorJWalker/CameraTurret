import cv2

class Application:
    def __init__(self, shouldRender):
        self.camera = cv2.VideoCapture(0)
        self.shouldRender = shouldRender

    def __del__(self):
        self.camera.close()

    def start(self):
        while True:
            success, frame = self.camera.read()

            if success:
                # run detector
            else:
                # print error
                print("Couldn't capture image")
