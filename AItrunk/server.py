# The core algorithm writing here
from modules.camera import Camera
from modules.controller import Controller






if __name__ == '__main__':
	camera = Camera()
	motor_pin = 17
	servo_pin = 16 # temp
	controller = Controller(motor_pin, servo_pin)
	#camera.face_detection()
