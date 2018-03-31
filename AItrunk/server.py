# The core algorithm writing here
from modules.camera import Camera
from modules.controller import Controller
from modules.DD import DD
import time





if __name__ == '__main__':
	camera = Camera()
	controller = Controller()
	D1 = DD(27)	#Front DD , obstacle detection
	D2 = DD(4)	##Back DD , person detection
	while(True):
            c = camera.test()
            print("The confidence : " + str(c))
            if(D1.status() == False):
                    # Obstacle has been detected
                    # stop
                    controller.Stop()
            elif(c < 0.2 and D1.status() == True):
                    # Front got no obstacle but do not dectect the face
                    # stop
                    controller.Stop()
            elif(c > 0.2 and D2.status() == True):
                    # Front got no obstacle and do detect the face but the person is out of the range
                    # stop
                    controller.Stop()
            else:
                    # Fron got no obstacle and do detect the face and the person is in the range
                    controller.Forward()

