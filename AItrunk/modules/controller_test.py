import RPi.GPIO as GPIO
import curses
import time
from curses import wrapper

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

stdscr = curses.initscr()
stdscr.clear()

while True:
    ch = stdscr.getkey()
# Quit 
    if ch == 'q':
       curses.endwin()
       GPIO.output(17, False)
       GPIO.output(18, False)
       GPIO.output(22, False)
       GPIO.output(23, False)
       break

# Forward
    if ch == 'w':
       GPIO.output(17, False)
       GPIO.output(18, True)
       GPIO.output(22, False)
       GPIO.output(23, True)

# Backward
    if ch == 'x':
       GPIO.output(17, True)
       GPIO.output(18, False)
       GPIO.output(22, True)
       GPIO.output(23, False)

# Turn Right
    if ch == 'd':
       GPIO.output(17, False)
       GPIO.output(18, True)
       GPIO.output(22, False)
       GPIO.output(23, False)

# Turn Left
    if ch == 'a':
       GPIO.output(17, False)
       GPIO.output(18, False)
       GPIO.output(22, False)
       GPIO.output(23, True)