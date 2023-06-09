# -*- coding: utf-8 -*-
"""
Created on Thu Feb  21 09:21:19 2022

@author: callum
"""
import cv2
import numpy as np

# Open Camera
camera = cv2.VideoCapture(0)
camera.set(10, 200)

hand = cv2.CascadeClassifier('haarcascades/Hand.Cascade.1.xml')

while camera.isOpened():
    #Main Camera
    ret, img = camera.read()
    
    if(ret):        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        palms = hand.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in palms:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
           
        cv2.imshow('Hand', img)
    
        k = cv2.waitKey(10)
        if k == 27:  # press ESC to exit
            break
    else:
        break
camera.release()
cv2.destroyAllWindows()