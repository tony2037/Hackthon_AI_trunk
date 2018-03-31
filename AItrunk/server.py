# The core algorithm writing here
from modules.camera import Camera
from modules.controller import Controller






if __name__ == '__main__':
	camera = Camera()
<<<<<<< HEAD
	motor_pin = 17
	servo_pin = 16 # temp
	controller = Controller(motor_pin, servo_pin)
	#camera.face_detection()
=======
	c = camera.face_detection()
	print(c)
>>>>>>> 4e3c12a9d2badff5dd7d7c83ed8a2aa0cbaf9e44
