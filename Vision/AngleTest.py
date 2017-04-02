#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:06:18 2017

@author: Edwin
"""

Ang_Path = 0.0
Ang_Center = 0.0
CenterPathX = 0
CenterPathY = 0
def receive(ang):
    Ang_Path = ang
    print Ang_Path

def recCenterAng(angle):
    Ang_Center = angle

def sendPath():
    return Ang_Path

def sendCenter():
    return Ang_Center

def centerX(xAxis):
    CenterPathX = xAxis

def centerY(yAxis):
    CenterPathY = yAxis

def sendX():
    return CenterPathX

def sendY():
    return CenterPathY
