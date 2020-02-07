import cv2

# Placeholder test code
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    cv2.imshow("Test", frame)
    if cv2.waitKey(1) & 0xFF == ord(u"\u0020"):
        break
