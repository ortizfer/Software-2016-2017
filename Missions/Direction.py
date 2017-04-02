# Object class for the direction of a point
class Direction(object):
    x = -1
    y = -1

    # The class constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_direction(x, y):
    direction = Direction(x, y)
    return direction

"""
VERSION CONTROL:

3- Fernando Ortiz 20/02/17
Direction Object creation and partial implementation

1- Fernando Ortiz 20/02/17
Initial Commit and creation of class.

"""