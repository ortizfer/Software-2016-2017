# functions that listen to the hydrophone and create the object direction and returns it to movement
from Missions import Direction


def listen():
    direction = Direction.Direction(0, 0)
    return direction

'''
VERSION CONTROL"

1- Carlos J. Figueroa 22/02/2017 5:26pm
    Added function listen(), returns a default direction object.
'''
