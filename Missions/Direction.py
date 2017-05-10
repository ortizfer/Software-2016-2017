'''
Direction Mission Logic. The file contains a definition for an object that represents direction.
Additionally it contains a function to create an object said type.
'''

'''
************************************************************************************************************************
Dictionary:
--Classes--
Direction(object): Contains the two attributes of x and y.
    init: takes parameters x and y, otherwise defaults to negative one.

--Functions--
make_direction(x, y): initializes a new object of type direction.
    parameter: int x, int y, the given directions
    return: the created object containing the given directions
************************************************************************************************************************
'''



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
4- Juan G. Lastra Febles and Carlos Figueroa 10/05/2017 6:41 PM
Edited the documentation

3- Fernando Ortiz 20/02/17
Direction Object creation and partial implementation

1- Fernando Ortiz 20/02/17
Initial Commit and creation of class.

"""