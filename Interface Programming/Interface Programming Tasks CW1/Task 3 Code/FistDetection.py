# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:48:02 2022

@author: callu
"""

import cv2 as cv
capture = cv.VideoCapture(0)# Opens Camera

pretrained_model = cv.CascadeClassifier("haarcascades/fist.xml")

while True:
    boolean, frame = capture.read()
    if boolean == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        coordinate_list = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 3)
        
        # Drawing a Rectangle in Frame
        for (x,y,w,h) in coordinate_list:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            
        # Display Detected Fist
        cv.imshow('Live Fist Detection', frame)
        
        # Condition to break out of the while loop
        if  cv.waitKey(20) == ord('x'):
            break
        
capture.release()
cv.destroyAllWindows()