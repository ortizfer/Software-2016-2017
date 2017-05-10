from Vision import AngleTest, FrameGrab
from Missions import Movement

''''
CenterPath Mission Logic. The functionality of the CenterPath is to align the submarine to the center of the path by
using different movements like perpendicular, parallel and align Y.

The start of this file is to identify the position of the submarine so it can change its position in a perpendicular
movement. By doing so it can align in th Y position and if the position is off, it can correct the submarines angle
relative to the path in a parallel fashion.

'''

'''
************************************************************************************************************************
Dictionary:

--variables--
x: global variable denoting a position
y: global variable denoting a position
parallelAngle: denotes the angle required to align the AUV in a parallel fashion to the path
turn: denotes the direction to rotate the AUV


--functions--
Start(): essentially the main function, orders all other functions to properly align the AUV
    parameter: void
    return: void
position(): modifies the global variables 'x' and 'y' to the current values
    parameter: void
    return: void
perpendicular(): aligns the AUV in a perpendicular fashion with the path marker in order to approach it
    parameter: void
    return: void
alignY(): moves the submarine forward and backwards until aligned with the path marker
    parameter: void
    return: void
parallel(): rotates the AUV in a parallel fashion to the path marker
    parameter: void
    return: void
centered(): returns a boolean if the AUV is properly centered with the path marker
    parameter: void
    return: boolean, whether the AUV is aligned or not

************************************************************************************************************************
'''

x = 0
y = 0
parallelAngle = 0
turn = ""


def Start():
    print("moving to center of path")
    position()
    perpendicular()
    alignY()
    parallel()
    alignY()
    # while not centered():
    #     print("moving to center of path")
    #     if x < 305 or x > 325:
    #         Movement.align(AngleTest.sendCenter())
    #     if y < 190:
    #         Movement.forward(2)
    #     if y > 210:
    #         Movement.backward(2)
    #     position()

    print("On top of the path center")


def position():
    x = AngleTest.sendX()
    y = AngleTest.sendY()
    parallelAngle = AngleTest.Ang_Path


def perpendicular():
    if parallelAngle > 0:
        Movement.align(parallelAngle - 90)
        turn = "left"
    else:
        Movement.align(parallelAngle + 90)
        turn = "right"


def alignY():
    while y < 190 or y > 210:
        if y < 190:
            Movement.forward(2)
        else:
            Movement.backward(2)
        position()


def parallel():
    if not centered():
        if x > 325:
            if parallelAngle > 0 and parallelAngle <= 90:
                Movement.align(parallelAngle)
            if parallelAngle < 0 and parallelAngle >= -90:
                Movement.align(parallelAngle + 180)
        else:
            if parallelAngle > 0 and parallelAngle <= 90:
                Movement.align(parallelAngle - 180)
            if parallelAngle < 0 and parallelAngle >= -90:
                Movement.align(parallelAngle)
    else:
        if turn == "left":
            Movement.align(90)
        else:
            Movement.align(-90)

    position()


def centered():
    if x < 305 or x > 325:
        return False
    elif y < 190 or y > 210:
        return False
    else:
        return True


'''
VERSION CONTROL:
1- Juan G. Lastra Febles and Carlos Figueroa 10/05/2017  4:28 PM
Documented the code




Author: Felix Gonzales
'''