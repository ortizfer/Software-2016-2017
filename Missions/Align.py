from Missions import Movement
from Vision import messPassing,FrameGrab

''''
This code is obsolete, needs update since is mixing with depth and align
'''
depth = 6
x = 0
y = 0
count = 0
fTurn = 0
def start():
    position()
    while not centered():
        if(y >= 200):
            depth = depth - 1
            Movement.depth(depth)
        elif(y <= 100):
            depth = depth + 1
            Movement.depth(depth)
        if(x >= 300):
            Movement.align(15)
            if count == 0:
                fTurn = 1
                count = count + 1

        elif (x <= 200) :
            Movement.align(-15)
            if count == 0:
                fTurn = -1
                count = count +1

        position()

def position():
    FrameGrab.frontFrame()
    # add bouy detection findBouy( bool, bool,bool)
    boya = messPassing.messPassing()
    boya = BoyasExoticas.start()
    x = boya.impBuoyX()
    y = boya.impBuoyY()

def centered():
    if x < 200 or x > 300:
        return False
    if y < 100 or y > 200:
        return False
    else:
        return True


def getFirstTurn():
    return fTurn


"""
VERSION CONTROL:
3- Juan G. Lastra Febles, Carlos Figueroa and Jose Montes  3:48 PM
commented in the code

2- Felix Gonzalez 8/03/2017 1:23pm
Tested functionality and improved time of execution.

1- Fernando Ortiz 2/03/17
Creation of version Control and print

"""
