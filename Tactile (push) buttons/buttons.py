import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_stateY = GPIO.input(20)
    if input_stateY == False:
        print('Yes button Pressed')
        time.sleep(0.2)

    input_stateN = GPIO.input(13)
    if input_stateN == False:
        print('No button Pressed')
        time.sleep(0.2)
