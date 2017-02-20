# Class to control the movement of the AUV

# Submerge the AUV to the desired depth
def submerge(depth):
    print("submerging to: " + depth)


# Move forward at a base 40% speed
def forward():
    print("moving at: 40%")


# Move forward at the desired speed
def forward_at(speed):
    print("moving at: " + speed)


# Move backward at a base 40% speed
def backward():
    print("Backing up at: 40%")


# Move backward at the desired speed speed
def backward_at(speed):
    print("Backing up at: " + speed)


"""
VERSION CONTROL:

2- Fernando Ortiz 19/02/17
Created basic movement functions for the AUV to use in the missions

1- Fernando Ortiz 19/02/17
Initial Commit and creation of class.

"""
