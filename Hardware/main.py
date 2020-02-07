from gpiozero import Servo
from time import sleep

# Placeholder test code
xServo = Servo(17)
yServo = Servo(18)

yServo.angle = 120
sleep(10)

while True:
    for i = 0 in range(180):
        xServo.angle = i
        sleep(2)

    for i = 100 in range(108, 0, -1):
        xServo.angle = i
