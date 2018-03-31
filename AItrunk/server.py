# The core algorithm writing here
from modules.camera import Camera
from modules.controller import Controller
from modules.DD import DD
import time





if __name__ == '__main__':
	camera = Camera()
	c = camera.test()
	print("The confidence : " + str(c))
	controller = Controller()

	D1 = DD()	#Front DD , obstacle detection
	D1_status = D1.status
	D2 = DD()	##Back DD , person detection
