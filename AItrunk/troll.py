import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(7, GPIO.RISING)
def my_callback():
        print GPIO.input(7)
        print "Gaga"
GPIO.add_event_callback(7, my_callback)


