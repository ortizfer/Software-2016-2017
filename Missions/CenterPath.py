from Vision import AngleTest, FrameGrab
from Missions import Movement

x = 0
y = 0
def Start():
    position()

    while not centered():
        print("moving to center of path")
        if x < 305 or x > 325:
            Movement.align(AngleTest.sendCenter())
        if y < 190:
            Movement.forward(2)
        if y > 210:
            Movement.backward(2)
        position()

    print("On top of the path center")

def position():
    x = AngleTest.sendX()
    y = AngleTest.sendY()


def centered():
    if x < 305 or x > 325:
        return False
    elif y < 190 or y > 210:
        return False
    else:
        return True