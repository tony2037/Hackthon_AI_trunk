# The core algorithm writing here
from modules.camera import Camera
from modules.controller import Controller
from modules.DD import DD
import time





if __name__ == '__main__':
    controller = Controller()
    D1 = DD(27)    #Front DD , obstacle detection
    D2 = DD(4)    ##Back DD , person detection
    while(True):
            if(D1.status() == False):
                    # Obstacle has been detected
                    # stop
                    controller.Stop()
            elif(D2.status() == True):
                    # did not detect person
                    # stop
                    controller.Stop()
            else:
                    # Fron got no obstacle and do detect the face and the person is in the range
                    controller.Forward()

