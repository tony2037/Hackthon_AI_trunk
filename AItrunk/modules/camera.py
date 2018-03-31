
#capture a photo
import os
import requests

class Camera(object):
    def __init__(self):
        print("success create a Camera object")

    def test(self):    
        os.system("fswebcam -r 640x360 -s 10 -d /dev/video0 webcam.jpg")

    def face_detection(self):
        os.system("fswebcam -r 640x360 -s 10 -d /dev/video0 webcam.jpg")

        #load image
        f = open('webcam.jpg','rb') 
        body = f.read() 
        f.close()

        #camera face detection


        headers_detection= {
            # Request headers
            'Content-type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': '07ecc20b5e0f4c01b3b62196a116fee6',
        }
        face_api_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'
        params_detection = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender'
        }

        response_detection = requests.post(face_api_url, params=params_detection, headers=headers_detection, data = body)

        if len(response_detection.json()) == 0:
            return -1
        else:
            detection_faceId = response_detection.json()[0]['faceId']
            top = response_detection.json()[0]['faceRectangle']['top']
            left = response_detection.json()[0]['faceRectangle']['left']
            width = response_detection.json()[0]['faceRectangle']['width']
            height = response_detection.json()[0]['faceRectangle']['height']

            #find
            headers_find = {
                # Request headers
                'Content-Type': 'application/json',
                'Ocp-Apim-Subscription-Key': '07ecc20b5e0f4c01b3b62196a116fee6',
            }
            json = {
                "faceId": detection_faceId,
                "faceListId": "trunk",
                "maxNumOfCandidatesReturned": 10,
                "mode": "matchPerson"
            }
            response_find = requests.post('https://westus.api.cognitive.microsoft.com/face/v1.0/findsimilars',json = json,headers = headers_find)
            #print(response_find.status_code)
            #print(response_find.json())
            find = response_find.json()
            confidence = 0
            for f in find:
                #print(f["confidence"])
                confidence = f["confidence"]
            return confidence
