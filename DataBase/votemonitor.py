#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import tm1637
import RPi.GPIO as GPIO
import time
import MySQLdb
import datetime

#import curses
#stdscr = curses.initscr()
#curses.noecho()
#curses.cbreak()

db = MySQLdb.connect(host="localhost", user="rpi", passwd="raspberry", db="voteDB")

GPIO.setwarnings(False)

# Initialize the display (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)

#initialize pins 26, 13 for yes, no input by tactile switch buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

Display.SetBrightness(0.8)
Display.Clear()
Display.ShowDoublepoint(True)     

y = 0
n = 0

print datetime.datetime.now()

def write2db( str ):
    curINS = db.cursor()
    try:
        sql = "INSERT INTO votes (name, email, moment, vote) VALUES ('in presence','null',now(),'"+str+"')"
        print sql
        curINS.execute(sql)
        db.commit()
    except:
        db.rollback()

    curINS.close()
    return

def readYes():
    #create a cursor for the select
    curSEL = db.cursor()
    #execute an sql query
    curSEL.execute("SELECT count(ID) FROM votes WHERE vote='y'")

    # loop to iterate
    for row in curSEL.fetchall() :
        #data from rows
        nai = str(row[0])
		
    # close the cursor
    curSEL.close()        
    return nai

def readNo():
    #create a cursor for the select
    curSEL = db.cursor()
    #execute an sql query
    curSEL.execute("SELECT count(ID) FROM votes WHERE vote='n'")

    # loop to iterate
    for row in curSEL.fetchall() :
        #data from rows
        oxi = str(row[0])
        
    # close the cursor
    curSEL.close()        
    return oxi

while True:
    input_stateY = GPIO.input(26)
    if input_stateY == False:
        write2db("y")
        print "Button for Yes pressed. We have %d Yes so far!" % (y)
        time.sleep(0.2)
    
    input_stateN = GPIO.input(13)
    if input_stateN == False:
        write2db("n")
        
        print "Button for No pressed. We have %d No so far!" % (n)
        time.sleep(0.2)

    time.sleep(0.1)
    
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

#source https://github.com/timwaizenegger/raspberrypi-examples
#source http://razzpisampler.oreilly.com/ch07.html
#source https://www.jeremymorgan.com/tutorials/python-tutorials/how-to-connect-to-mysql-with-python/
#source https://docs.python.org/2/howto/curses.html#curses-howto