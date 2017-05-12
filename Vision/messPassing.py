#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:57:50 2017

@author: Felix Gonzalez
"""

class messPassing:
    
    def __init__ (self):
        anglePath = 0
        centerPathX = 0
        centerPathY = 0
        centerBuoyX = 0
        centerBuoyY = 0
        foundPath = 1

    def foundP(self,found):
        self.foundPath = found

    def angle(self,Angle):
        self.anglePath = Angle
        
    def pathX(self, centerPathX):
        self.centerPathX = centerPathX
        
    def pathY (self, centerPathY):
        self.centerPathY = centerPathY
        
    def buoyX (self, centerBuoyX):
        self.centerBuoyX = centerBuoyX
        
    def buoyY (self, centerBuoyY):
        self.buoyY = centerBuoyY
        
    def impAngle(self):
        return self.anglePath
    
    def impPathX(self):
        return self.centerPathX

    def impPathY(self):
        return self.centerPathY
    
    def impBuoyX(self):
        return self.centerBuoyX
    
    def impBuoyY(self):
        return self.centerBuoyY

    def impFound(self):
        return self.foundPath
