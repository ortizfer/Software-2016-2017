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
CenterBuoyX = 0
CenterBuoyY = 0
def receive(ang):
    Ang_Path = ang
    print(Ang_Path)

def recCenterAng(angle):
    Ang_Center = angle

def sendPath():
    return Ang_Path

def sendCenter():
    return Ang_Center

def centerPathX(xAxis):
    CenterPathX = xAxis

def centerBuoyY(yAxis):
    CenterBuoyY = yAxis

def centerBuoyX(xAxis):
    CenterBuoyX = xAxis

def centerPathY(yAxis):
    CenterPathY = yAxis

def sendPathX():
    return CenterPathX

def sendPathY():
    return CenterPathY

def sendBuoyX():
    return CenterBuoyX

def sendBuoyY():
    return CenterBuoyY