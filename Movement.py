# Class to control the movement of the AUV
import time
import Direction
# import SerialCom


# Submerge the AUV to the desired depth
def submerge(depth):
    print("submerging to: " + depth)
    # SerialCom.write0(depth)
    # SerialCom.write1(depth)


# Surface de desired feet
def surface(depth):
    print("going up: " + depth + " feet")
    # SerialCom.write0(depth)
    # SerialCom.write1(depth)


# Move forward at a base 40% speed
def forward(seconds):
    print("moving at: 40%")
    # SerialCom.write0()
    # SerialCom.write1()
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1


# Move forward at the desired speed
def forward_at(speed, seconds):
    print("moving at: " + speed)
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1


# Move backward at a base 40% speed
def backward(seconds):
    print("Backing up at: 40%")
    # SerialCom.write0()
    # SerialCom.write1()
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1


# Move backward at the desired speed speed
def backward_at(speed, seconds):
    print("Backing up at: " + speed)
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1


# Original movement for Gate2 mission
def do_magic():
    print("Doing a cool stunt")


# Stop AUV
def stop():
    print("stopping")
    seconds = 10
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1


# Get depth from the pressure sensor
def get_depth():
    return 4.0
    # SerialCom.read0()
    # SerialCom.read1()


# Align heading of the AUV
def align():
    print("align check")


# Get the direction (angle, vector) of where to move
def get_direction():
    direction = Direction.make_direction(0, 0)
    return direction

"""
VERSION CONTROL:

3- Fernando Ortiz 20/02/17
Added more functions for the movement utilities

2- Fernando Ortiz 19/02/17
Created basic movement functions for the AUV to use in the missions

1- Fernando Ortiz 19/02/17
Initial Commit and creation of class.

"""
