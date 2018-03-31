
#capture a photo
import os
import requests

def face_detection():
    os.system("fswebcam -r 640x360 -S 10 -d /dev/video0 webcam.jpg")

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
    detection_faceId = response_detection.json()[0]['faceId']
    #print(detection_faceId)
    #print(response_detection.status_code)
    #print(response_detection.json())

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
    print(response_find.status_code)
    print(response_find.json())
    find = response_find.json()
    confidence = 0
    for f in find:
        #print(f["confidence"])
        confidence = f["confidence"]
    return confidence
