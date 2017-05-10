
# INCOMPLETE, requires the hydrophone hardware to be finished #

'''
Hydrophone Mission logic. functions that listen to the hydrophone and create the object directon and returns it to
movement.
'''

# functions that listen to the hydrophone and create the object direction and returns it to movement
from Missions import Direction


def listen():
    direction = Direction.Direction(0, 0)
    return direction

'''
VERSION CONTROL"

2- Juan G. Lastra Febles and Carlos Figueroa 10/05/2017  3:56 PM
commented on the code

1- Carlos J. Figueroa 22/02/2017 5:26pm
    Added function listen(), returns a default direction object.
'''
