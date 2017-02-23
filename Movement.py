# Class to control the movement of the AUV
import time
import Direction
import Hydrophone
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


# Rotates the entered angles COUNTER-CLOCKWISE
def left(angle):
    print("moving left " + str(angle) + " degrees")


# Rotates the entered angles CLOCKWISE
def right(angle):
    print("moving right " + str(angle) + " degrees")


# Original movement for Gate2 mission.
# Currently moves in reverse for the specified time.
def do_magic(seconds):
    print("Doing a cool stunt")
    left(180)
    backward(seconds)
    right(180)


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


# Function to touch the buoy
def bop_it():
    print("Touching the Buoy")


# Listen the hydrophones
def listen():
    print("Listening for hydrophones")
    Hydrophone.listen()

"""
VERSION CONTROL:

7- Carlos J. Figueroa 23/02/2017 5:57pm
Implemented the do_magic function. Added an angle parameter for left() and right()

6- Fernando Ortiz 22/02/17
FUnction left and right added

5- Carlos J. Figueroa 22/02/2017 5:30pm
Added hydrophone import.

4- Fernando Ortiz 22/02/17
created additional functions listen and bop_it for logic on missions

3- Fernando Ortiz 20/02/17
Added more functions for the movement utilities

2- Fernando Ortiz 19/02/17
Created basic movement functions for the AUV to use in the missions

1- Fernando Ortiz 19/02/17
Initial Commit and creation of class.

"""
