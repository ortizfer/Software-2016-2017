from Vision import AngleTest, FrameGrab
from Missions import Movement

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