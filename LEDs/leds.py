#! /usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Gled = 18
Yled = 24
Rled = 25

GPIO.setup(Gled, GPIO.OUT)
GPIO.setup(Yled, GPIO.OUT)
GPIO.setup(Rled, GPIO.OUT)

while True:
	GPIO.output(Gled,True)
	time.sleep(1)
	GPIO.output(Gled,False)

	GPIO.output(Yled,True)
	time.sleep(1)
	GPIO.output(Yled,False)

	GPIO.output(Rled,True)
	time.sleep(1)
	GPIO.output(Rled,False)