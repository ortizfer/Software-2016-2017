#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:30:24 2017

@author: Edwin
"""
#
#import cv2
#import numpy as np
#cap = cv2.VideoCapture(0)
#
#def captureFrame():
#    
#    ret, frame  = cap.read()
#    cv2.imwrite("frame%d.jpg", cap)
#    cap.release()
#    return cap
#
#captureFrame()


import cv2
import numpy as np
import time

counter = 0
 
cap = cv2.VideoCapture(0)
#while True = multiples fotos
while counter < 2:
    
    ret, frame  = cap.read()
    time.sleep(3)
    cv2.imwrite("path%d.jpg" % counter,frame)
    counter +=1
    print counter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
execfile('Path.py')    
    
    
cap.release()
cv2.destroyAllWindows()  

