# Class to control the movement of the AUV
import time

from Missions import Direction

from Missions import Hydrophone


from Utils import SerialCom
from Utils import Parser
from Vision import FrameGrab
from Vision import AngleTest

commands = {
    "depth": 'o',
    "alignment": 'a',
    "exit": 'x',
    "forward": 'f',
    "backward": 'b',
    "HCw": 'w',
    "HCa": 'a',
    "HCs": 's',
    "HCd": 'd',
    "printUser": 't',
    "printScript": 'y'
}




# Submerge the AUV to the desired depth
def depth(extent):
    print("submerging to: " + extent)
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPUP(commands["depth"])
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPUP())

    SerialCom.writeMSPUP(extent)
    time.sleep(0.5)
    feedback = SerialCom.readMSPUP()

# Align the AUV with the path.
def align(Angle) :
    print("Alignment")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPUPFRONT(commands["aligment"])
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPUPFRONT())

    SerialCom.writeMSPFRONT(Angle)
    time.sleep(0.5)
    feedback = SerialCom.readMSPFRONT()

# Move forward at a base 40% speed
def forward(seconds):
    print("moving at: 40%")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPFRONT(commands["forward"])
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPFRONT())
    SerialCom.writeMSPFRONT(seconds)
    time.sleep(0.5)
    feedback = SerialCom.readMSPFRONT()
'''
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1
'''


# Move backward at a base 40% speed
def backward(seconds):
    print("Backing up at: 40%")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPFRONT(commands ['backwards'])
        time.sleep(0.5)
        feedback =Parser.p_slice(SerialCom.readMSPFRONT())
    SerialCom.writeMSPFRONT(seconds)
    time.sleep(0.5)
    feedback = SerialCom.readMSPFRONT()
'''
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1
'''

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
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPFRONT(commands['exit'])
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.writeMSPFRONT())




# Get depth from the pressure sensor
def get_depth():
    return 4.0
    # SerialCom.read0()
    # SerialCom.read1()



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
    return Hydrophone.listen()


# Return x or y axis position
def getAngle(axis):
    if(axis == "yaw"): # x axis
        print("yaw")
        return 0

    if (axis == "pitch"): # y axis
        print("pitch")
        return 0
    return 0

#Align commands with picture data
def moveUp(pitch):
    return pitch + 10;

def moveDown(pitch):
    return pitch - 10;

def moveLeft(yaw):
    return yaw - 10;

def moveRight(yaw):
    return yaw + 10;

def rotate():
    print("")

"""
VERSION CONTROL:
11 - Juan G.Lastra and Estaban Lopez 1/04/2017 6:10 P.M
Alterated the forward, badkward and stop functions and eliminated forward a and backward a.

10 - Juan G. Lastra Febles and Carlos J. Figueroa 14/03/2017 8:30 P.M
Changed and edited the SerialCom write and read for the submerged, surface, front, up and back functions

9- Felix Gonzalez 8/03/2017 1:23pm
Added and partially implemented:
    - moveUp
    - moveDown
    - moveLeft
    - moveRight

8- Carlos J. Figueroa 01/03/2017 7:03pm
Added submerge_check function.

7- Carlos J. Figueroa 23/02/2017 3:57pm
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
