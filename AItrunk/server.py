# The core algorithm writing here
from modules.camera import Camera
from modules.controller import Controller
from modules.DD import DD
import time
from multiprocessing import Process
import os
def request_img():
    camera = Camera()
    controller = Controller()
    D1 = DD(27)
    D2 = DD(4)
    while(1):
        if(camera.face_detection() > 0.2 and D2==False and D1==True):
            controller.Forward()

def detect_distance():
    controller = Controller()
    D1 = DD(27)
    D2 = DD(4)
    while(1):
        if(D1.status() == False):
            controller.Stop()
        elif(D2.status() == True):
            controller.Stop()




if __name__ == '__main__':
    p = Pool()
    p.apply_async(request_img)
    p.apply_async(detect_distance)
