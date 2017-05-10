# Class to control the movement of the AUV
import time

from Missions import Direction

from Missions import Hydrophone

from Utils import SerialCom
from Utils import Parser
from Vision import FrameGrab
from Vision import AngleTest

'''
Movement Mission Logic. Provides the functionality of the movement of the AUV (Autonomous Underwater Vehicle) with
different movements that are related to Depth and Align.

In the Depth control, it provides in how much depth is desired, how to stop is submerge and how to obtain new values for
the submarine to change in feet its depth in the water.

In the Align control, it provides how to start the Align process, in how to control the speed that is in 40% of power in
forward and backward movements. How to stop the Align process, set new points of directions for the submarine, gain new
values to Align and to converge the sensor errors using threshold.

Other features in the code is to rotate in the angles received for the submarine in Counter-Clockwise and Clockwise.
By using the picture taken by the submarine it can move or rotate to Align.

'''



commands = {
    "depth": 'os',
    "alignment": 'as',
    "exitA": 'ax',
    "exitD": 'ox',
    "forward": 'f',
    "backward": 'b',
    "startA": 'an',
    "startD": 'on',
    "gainA": 'ag',
    "gainD": 'og',
    "set": 'am',
    "forT": 'tf',
    "AlT": 'tg',
    "genT": 'th',
    "HCw": 'w',
    "HCa": 'a',
    "HCs": 's',
    "HCd": 'd',
    "printUser": 't',
    "printScript": 'y'
}

"""
*****************************************************************************
DICTIONARY:
Align:
j- enciende el output continuo
k- apaga el output
an - prende controlador - DONE
ax - apaga el controlador  - DONE
am - setpoint actual (set to actual value)  - DONE
as(X) - setpoint neg izq pos derecha 1-9 q-y(y=60)  - DONE
ag(X) - 0-9 gain - DONE
ad - cambia la polaridad de los motores 
tf(X) - 0-9 treshhold de desalineacion en forward  - DONE
tg(X) - 0-9 grados para salir del align forward (grados de error)- DONE
th - treahhold comotal del align controler - DONE
f(T) - forward por T tiempo  - DONE
b(T) -  backwards por T tiempo  - DONE

Depth:
j- enciende el output continuo
k- apaga output
on - prende el controlador  - DONE
ox - apaga el controlador  - DONE
od - cambia el bias 1 vez 14.5 2 veces 29.5 bias
os(X) - 0-9 profundidad en pies q-11 w-12 etc.  - DONE
og(X) - 0-9 ganancia  - DONE
***************************************************************************** 
"""

"""
*****************************************************************************
Controlador de Profundidad
*****************************************************************************
"""


# Submerge the AUV to the desired depth
def depth(extent):
    print("submerging to: " + extent)
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPUP(commands["depth"] + extent + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPUP())


# Stop Depth
def stopD():
    print("stopping depth controller")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPUP(commands["exitD"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.writeMSPUP())


# Start Depth
def startD():
    print("starting depth controller")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPUP(commands["startD"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.writeMSPUP())


def gainD(value):
    print("new depth gain: " + value)
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPUP(commands["gainD"] + value + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.writeMSPUP())


"""
******************************************************************************
Controlador de Align
******************************************************************************
"""


# Start align controller
def startA():
    print("Starting Align Controller")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPFRONT(commands["startA"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPUPFRONT())


# Gain of the Align

def gainA(value):
    print("Changing Align Gain: " + value)
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPFRONT(commands["gainA"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPUPFRONT())


# Align the AUV with the path.
def align(Angle):
    print("Alignment")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPUPFRONT(commands["alignment"] + Angle + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPUPFRONT())


# Move forward at a base 40% speed
def forward(seconds):
    print("moving at: 40%")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPFRONT(commands["forward"] + seconds + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPFRONT())


# Move backward at a base 40% speed
def backward(seconds):
    print("Backing up at: 40%")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPFRONT(commands["backwards"] + seconds + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPFRONT())


# Stop ALign
def stopA():
    print("stopping")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPFRONT(commands["exitA"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.writeMSPFRONT())


def setPoint():
    print("set new point")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPFRONT(commands["set"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.writeMSPFRONT())

# To converge the error of the sensor
def treshA():
    print("Setting Align Tresholds")
    feedback = 'i'
    while feedback != 'f':
        SerialCom.writeMSPFRONT(commands["forT"] + '' + '/n')
        time.sleep(0.5)
        SerialCom.writeMSPFRONT(commands["AlT"] + '' + '/n')
        time.sleep(0.5)
        SerialCom.writeMSPFRONT(commands["genT"] + '' + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPUPFRONT())


"""
****************************************************************************
"""


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
    if (axis == "yaw"):  # x axis
        print("yaw")
        return 0

    if (axis == "pitch"):  # y axis
        print("pitch")
        return 0
    return 0


# Align commands with picture data
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
13- Juan G. Lastra 10/05/2017  3:01 PM
Documented the code

12 - Fernando / Tahiri 5/5/2017 3:37 PM
Fixed and added all controller functions

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
