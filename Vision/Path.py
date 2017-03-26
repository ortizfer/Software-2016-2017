#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:16:46 2017

@author: Edwin
""" #q2 = angle-90
    #q1 = 90 - angle
""" Tomar foto de la boya a la distancia mayor para determinar el area minima del rect
que estoy buscando"""
import cv2
import numpy as np
import math 
import AngleTest

def pathAngle(vectA1,vectA2,VectB1,VectB2):
    a = a1-a2
    b = b1-b2
    vDot = np.dot(a,b)
    a1Sqr = a[0]
    a2Sqr = a[1]
    aSqr = np.sqrt(a1Sqr **2 + a2Sqr **2)
    bSqr = 630
    angle = vDot/aSqr
    angle = angle/bSqr
    angleRad = math.acos(angle)
    angleDeg = 180 -((angleRad *180)/math.pi)
    AngleTest.receive(angleDeg)
    return angleDeg
    
#angleDeg =0   
contours = np.array([])
hierarchy = np.array([])
a1 = np.array([])
a2 = np.array([])
b1 =np.array ([0,200])
b2 = np.array([630,200])
pathIm = cv2.imread("path1.jpg")
contour_List1 = [] 
pathIm= cv2.resize(pathIm,(630,400))
pathIm2 = pathIm.copy()
pathIm2 = cv2.cvtColor(pathIm2, cv2.COLOR_BGR2GRAY)
Filt_path = cv2.bilateralFilter(pathIm,7,900,900)

path_edges = cv2.Canny(Filt_path, 0,100, True)
k = 0
ID =0
count =0
contours, hierarchy = cv2.findContours(path_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE, contours, hierarchy)

for contour in contours:
    approxV = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour,True),True)
    if (( 4 <= len(approxV) <= 8)) :
        contour_List1.append(contour)
         
if not len(contour_List1) == 0:
    for cnt in contour_List1:
        count +=1
        kcomp = len(cnt)
        if kcomp > k:
            k = kcomp
            ID = count - 1             
        else: 
            k = k
       
        #k = (max(cnt, key=len))
        
    
#k = len(contours) -1
rect = cv2.minAreaRect(contour_List1[ID])
box = cv2.cv.BoxPoints(rect)
box = np.int0(box)
cv2.drawContours(pathIm,[box],0,(0,0,255),2)

a1 = np.array(box[2]) 
a2 = np.array(box[3])

path_Angle = pathAngle(a1,a2,b1,b2)

font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(pathIm,'128.41 ',(0,130), font, 1, (200,255,155), 2)

cv2.line(pathIm, (box[2][0],box[2][1]),(box[3][0],box[3][1]),(0,255,255),2)
cv2.line(pathIm, (0,200),(630,200),(255,255,255),2)
cv2.imshow("EdgeMap",path_edges)
cv2.imshow("Rectangle", pathIm)
#cv2.imwrite("Angle Image", pathIm)
cv2.waitKey(0)
cv2.destroyAllWindows () 