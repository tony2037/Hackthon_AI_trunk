import RPi.GPIO as GPIO
class DistanceDecet(pin):
    def status():
        return GPIO.input(pin)
    def callback(my_callback):
        GPIO.add_event_detect(pin, GPIO.RISING)
        GPIO.add_event_callback(pin, my_callback)
def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
if  __name__ =='__main__':
    main()
