#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import tm1637
import RPi.GPIO as GPIO
import time
import MySQLdb
import datetime

db = MySQLdb.connect(host="localhost", user="rpi", passwd="raspberry", db="voteDB")

GPIO.setwarnings(False)

#initialize pins 26, 13 for yes, no input by tactile switch buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def write2db( str ):
    curINS = db.cursor()
    sql = "INSERT INTO voteDB.votes (name, email, moment, vote) VALUES ('in presence','null',now(),'"+str+"')"
    curINS.execute(sql)
    curINS.close()
    return

while True:
    input_stateY = GPIO.input(26)
    if input_stateY == False:
        write2db("y")
        print "Vote Yes recorded. Thank you!"
        time.sleep(0.1)
    
    input_stateN = GPIO.input(13)
    if input_stateN == False:
        write2db("n")
        print "Vote No recorded. Thank you!"
        time.sleep(0.1)


db.close() # close the connection
		
#source https://github.com/timwaizenegger/raspberrypi-examples
#source http://razzpisampler.oreilly.com/ch07.html
#source https://www.jeremymorgan.com/tutorials/python-tutorials/how-to-connect-to-mysql-with-python/
#source https://docs.python.org/2/howto/curses.html#curses-howto