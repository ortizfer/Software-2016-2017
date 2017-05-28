# Class to control the movement of the AUV
import time

from Utils import SerialCom, Parser


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
************************************************************************************************************************
DICTIONARY:

--Depth Controller--
depth(extent): Is a function that changes the depth of the AUV to the given value. It uses the following strings as the
serialcom parameters:
j- enciende el output continuo
k- apaga output
on - prende el controlador  - DONE
ox - apaga el controlador  - DONE
od - cambia el bias 1 vez 14.5 2 veces 29.5 bias
os(X) - 0-9 profundidad en pies q-11 w-12 etc.  - DONE
og(X) - 0-9 ganancia  - DONE
    parameter: int; the absolute depth value to move to, given in feet
    return: void

stopD(): stops the depth controllers
    parameter: void
    return: void
startD(): starts the depth controllers
    parameter: void
    return: void
gainD(value): modifies the depth controllers gain
    parameter: char; the controller gain, modifies the motor's power
    return: void
-/Depth Controller/-


--Align Controller--
startA(): starts the align controllers
    parameter: void
    return: void
gainA(value): modifies the align controllers gain
    parameter: char; the controllers gain, modifies the motor's power
    return: void
align(Angle): Is a function that rotates the AUV to the given angle. This function takes the following strings as serialcom
parameters:
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
    parameter: int; rotates the given angle relative to the AUV's current heading
    return: void

forward(seconds): Turns on the AUV motors to move forward for the given amount of time.
    parameter: int; the amount of time the AUV will move
    return: void
backward(): Turns on the AUV motors to move backwards for the given amount of time.
    parameter: int, seconds; the amount of time the AUV will move
    return: void
stopA(): stops the align controllers
    parameter: void
    return: void
setPoint(): the current position is made into the new setpoint
    parameter: void
    return: void

treshA(): PENDING
-/Align Controller/-

--Other Misc--
left(angle): PENDING
right(angle): PENDING
do_magic(seconds): PENDING
get_depth(): PENDING
get_direction(): PENDING
bop_it(): PENDING
listen(): PENDING
getAngle(axis): PENDING
moveUp(pitch): PENDING
moveDown(pitch): PENDING
moveLeft(yaw): PENDING
moveRight(yaw): PENDING
rotate(): PENDING
-/Other Misc/-

************************************************************************************************************************
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
    while feedback != 'v':
        SerialCom.writeMSPUP(commands["depth"] + extent + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPUP())


# Stop Depth
def stopD():
    print("stopping depth controller")
    feedback = 'i'
    while feedback != 'v':
        SerialCom.writeMSPUP(commands["exitD"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.writeMSPUP())


# Start Depth
def startD():
    print("starting depth controller")
    feedback = 'i'
    while feedback != 'v':
        SerialCom.writeMSPUP(commands["startD"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.writeMSPUP())


def gainD(value):
    print("new depth gain: " + value)
    feedback = 'i'
    while feedback != 'v':
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
    while feedback != 'v':
        SerialCom.writeMSPFRONT(commands["startA"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPFRONT())


# Gain of the Align

def gainA(value):
    print("Changing Align Gain: " + value)
    feedback = 'i'
    while feedback != 'v':
        SerialCom.writeMSPFRONT(commands["gainA"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPFRONT())


# Align the AUV with the path.
def align(Angle):
    print("Alignment")
    feedback = 'i'
    while feedback != 'v':
        SerialCom.writeMSPFRONT(commands["alignment"] + Angle + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPFRONT())


# Move forward at a base 40% speed
def forward(seconds):
    print("moving at: 40%")
    feedback = 'i'
    while feedback != 'v':
        SerialCom.writeMSPFRONT(commands["forward"] + seconds + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPFRONT())


# Move backward at a base 40% speed
def backward(seconds):
    print("Backing up at: 40%")
    feedback = 'i'
    while feedback != 'v':
        SerialCom.writeMSPFRONT(commands["backwards"] + seconds + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPFRONT())


# Stop ALign
def stopA():
    print("stopping")
    feedback = 'i'
    while feedback != 'v':
        SerialCom.writeMSPFRONT(commands["exitA"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.writeMSPFRONT())


def setPoint():
    print("set new point")
    feedback = 'i'
    while feedback != 'v':
        SerialCom.writeMSPFRONT(commands["set"] + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.writeMSPFRONT())

# To converge the error of the sensor
def treshA():
    print("Setting Align Tresholds")
    feedback = 'i'
    while feedback != 'v':
        SerialCom.writeMSPFRONT(commands["forT"] + '2' + '/n')
        time.sleep(0.5)
        SerialCom.writeMSPFRONT(commands["AlT"] + '2' + '/n')
        time.sleep(0.5)
        SerialCom.writeMSPFRONT(commands["genT"] + '1' + '/n')
        time.sleep(0.5)
        feedback = Parser.p_slice(SerialCom.readMSPFRONT())


"""
****************************************************************************
"""



"""
VERSION CONTROL:
14- Juan G. Lastra Febles and Carlos Figueroa 10/05/2017 5:45 PM
Edited the documentation

13- Juan G. Lastra Febles 10/05/2017  3:01 PM
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
