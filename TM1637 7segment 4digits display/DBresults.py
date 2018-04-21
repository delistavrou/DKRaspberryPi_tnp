#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import tm1637
import RPi.GPIO as GPIO
import time
import MySQLdb
import datetime

GPIO.setwarnings(False)

# Initialize the display (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)

Display.SetBrightness(0.8)
Display.Clear()
Display.ShowDoublepoint(True)     

db = MySQLdb.connect(host="localhost", user="rpi", passwd="raspberry", db="voteDB")
curSEL = db.cursor()

def readYes():
    curSEL.execute("SELECT count(ID) FROM votes WHERE vote='y'")
    row = curSEL.fetchone ()
    nai = str(row[0])
    return nai

def readNo():
    curSEL.execute("SELECT count(ID) FROM votes WHERE vote='n'")
    row = curSEL.fetchone ()
    oxi = str(row[0])
    return oxi

while True:
    db = MySQLdb.connect(host="localhost", user="rpi", passwd="raspberry", db="voteDB")
    y = int(readYes())
    Ydecades = y / 10
    Yunits   = y % 10
    Display.Show1(0, Ydecades)
    Display.Show1(1, Yunits)
    
    n = int(readNo())
    Ndecades = n / 10
    Nunits   = n % 10
    Display.Show1(2, Ndecades)
    Display.Show1(3, Nunits)
    
    time.sleep(0.5)
	        
curSEL.close()        
db.close() # close the connection

#db.close() # close the connection
#db.close() # close the connection

#source https://github.com/timwaizenegger/raspberrypi-examples
#source http://razzpisampler.oreilly.com/ch07.html
#source https://www.jeremymorgan.com/tutorials/python-tutorials/how-to-connect-to-mysql-with-python/
#source https://docs.python.org/2/howto/curses.html#curses-howto