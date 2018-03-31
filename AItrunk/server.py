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

	D1 = DD(27)	#Front DD , obstacle detection
	D1_status = D1.status
	D2 = DD(4)	##Back DD , person detection

	while(True):
		if(D1.status == False):
			# Obstacle has been detected
			None
		elif(camera.test() < 0.2):
			# Front got no obstacle but do not dectect the face
			None
		elif(D2.status == True):
			# Front got no obstacle and do detect the face but the person is out of the range
			None
		else:
			# Fron got no obstacle and do detect the face and the person is in the range
			None

