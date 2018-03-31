# motor and servo 
from RPi import GPIO as gpio
import time

class Controller(object):
  def __init__(self):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    print("Controller has been constructed")

  def Forward(self):
    GPIO.output(17, False)
    GPIO.output(18, True)
    GPIO.output(22, False)
    GPIO.output(23, True)

  def Backward(self):
    GPIO.output(17, True)
    GPIO.output(18, False)
    GPIO.output(22, True)
    GPIO.output(23, False)

  def Right(self):
    GPIO.output(17, False)
    GPIO.output(18, True)
    GPIO.output(22, False)
    GPIO.output(23, False)

  def Left(self):
    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.output(22, False)
    GPIO.output(23, True)

  def Stop(self):
    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.output(22, False)
    GPIO.output(23, False)

  def Quit(self):
    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.output(22, False)
    GPIO.output(23, False)
    GPIO.cleanup()