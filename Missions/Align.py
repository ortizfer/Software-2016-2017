from Missions import Movement
from Vision import AngleTest,FrameGrab

x = 0
y = 0
def start():
    position()
    while not centered():
        if(y >= 200):
            Movement.depth("&d", Movement.get_depth() - 1)
        elif(y <= 100):
            Movement.depth("&d", Movement.get_depth() + 1)
        if(x >= 300):
            Movement.align(15)
        elif (x <= 200) :
            Movement.align(-15)
        FrameGrab.frontFrame()
        position()

def position():
    x = AngleTest.sendX()
    y = AngleTest.sendX()

def centered():
    if x < 200 or x > 300:
        return False
    if y < 100 or y > 200:
        return False
    else:
        return True



"""
VERSION CONTROL:
2- Felix Gonzalez 8/03/2017 1:23pm
Tested functionality and improved time of execution.

1- Fernando Ortiz 2/03/17
Creation of version Control and print

"""
