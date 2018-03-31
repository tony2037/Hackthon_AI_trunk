import RPi.GPIO as GPIO
class DistanceDecet(pin):
    def status():
        return GPIO.input(pin)

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING)
if  __name__ =='__main__':
    main()
