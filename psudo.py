while(1):
    set_timeout(1/60):
        cameara.open()
        img = cameara.cature("foo.jpg")
        face_x1,face_x2,face_confidence = request("microsoft face api",img) #face 是一個信心值
        x1,y1, x2,y2,class_confidence= request("microsoft thing api") #給我bounding box 跟那個class的信心
        width = cameara.width()
        div_width = width/2 #得到相機的中心點
        box_center = (x1+x2)/2 #得到bounding box 的中心
        box_distance = box_center-div_width #得到bouning box 跟中心點的距離
        distance_with_face = redlight_api()
        distance_with_object = redlight_api()
        if(distance_with_face > 5):
            car.forward()
        if(distance_with_face < 5):
            car.stop()
        if(distance_with_object > 5):
            car.forward()
        if(distance_with_object < 5) :
            car.stop()
        """ #for 轉彎功能
        if(-1 < box_distance < 0):
            car.right()
        if(0 < box_distance < 1):
            car.left()
        elif(-5 < box_distance < -1):
            car.forward()
        elif(1 < box_distance < 5):
            car.forward()
        """



