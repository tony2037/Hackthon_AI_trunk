import RPi.GPIO as GPIO
class DD:
    def __init__(self,pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
    def status(self):
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        return  GPIO.input(self.pin)
    def callback(self,my_callback):
        GPIO.add_event_detect(self.pin, GPIO.RISING)
        GPIO.add_event_callback(self.pin, my_callback)
