class Direction(object):
    angle = -1
    vector = -1

    # The class "constructor" - It's actually an initializer
    def __init__(self, angle, vector):
        self.angle = angle
        self.vector = vector


def make_direction(angle, vector):
    direction = Direction(angle, vector)
    return direction

"""
VERSION CONTROL:

3- Fernando Ortiz 20/02/17
Direction Object creation and partial implementation

1- Fernando Ortiz 20/02/17
Initial Commit and creation of class.

"""