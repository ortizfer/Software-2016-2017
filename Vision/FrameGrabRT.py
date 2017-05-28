#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 08:51:46 2017

@author: Edwin
"""

import cv2
import numpy as np
from Missions import Movement

blueLow = 0
greenLow =63
redLow = 167
blueUp = 82
greenUp = 95
redUp = 255

BGRLOW=np.array([blueLow,greenLow,redLow])
BGRUPP=np.array([blueUp,greenUp,redUp])
contours = np.array([])
hierarchy = np.array([])
contour_List1 = [] 
cap = cv2.VideoCapture(0)
count = 0

def startLive():

    while(count <=3):
        _,frame=cap.read()

        frame = cv2.resize(frame,(630,400))

        BGRLow=np.array([blueLow,greenLow,redLow])
        BGRUp=np.array([blueUp,greenUp,redUp])
        mask = cv2.inRange(frame,BGRLow, BGRUp)

        #Calculate Edge Map'
        path_edges = cv2.Canny(mask, 0,100, True)
        #Find Contours'
        contours, hierarchy = cv2.findContours(path_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE, contours, hierarchy)
        #Check if contours were found'
        if len(contours) ==0:
            print "Adjust canny"
            Movement.forward('0')
        #Look for a rectangle'
        for contour in contours:
            approxV = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour,True),True)
            if cv2.contourArea(contour) > 50:#if path is x big might need to adjust

                if (len(approxV) >= 3 and len(approxV) <= 6 ):
    #
                #if (( 4 <= len(approxV) <= 6)) :
                    print len(approxV)
                    print "Rectangle found"
                    count =count+1

                    contour_List1.append(contour)
                else:
                    print "No rectangle found"
                    count = 0
                    Movement.forward('0')

    #        'Check if rectangle were found'
    #        if len(contour_List1) == 0:
    #            print "No rectangle found"
    #        else:
    #            print "Found!"

    #            y, x = np.nonzero(path_edges)
    #            x = x - np.mean(x) #Substracting x - xmean for stability
    #            y = y - np.mean(y)#Substracting y - ymean for stability
    #
    #            coords = np.vstack([x, y])
    #            cov = np.cov(coords) #Covariance Matrix
    #            evals, evecs = np.linalg.eig(cov) #EigenValues and EigenVectors
    #            sort_indices = np.argsort(evals)[::-1] #Sort EigenValues in decreasing order
    #            evec1, evec2 = evecs[:, sort_indices]
    #            x_v1, y_v1 = evec1  # Eigenvector with largest eigenvalue
    #            x_v2, y_v2 = evec2
    #            theta = np.tanh((x_v1)/(y_v1))
    #            theta = theta*100 #Angle for control system
    #            print theta
        cv2.imshow('yay', mask)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    """
    
    ADD STOP AUV
    
    """
    cv2.destroyAllWindows()