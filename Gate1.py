# Gate1 Mision

# Import movement dependencies
import Movement

# start mission logic
def start():

    print("Starting Gate1 mission")
    # Submerge the AUV to 2 feet
    Movement.submerge("2")

    # Full 40% forward
    Movement.forward()

    print("exiting Gate1")



"""
VERSION CONTROL:

2- Fernando Ortiz 19/02/17
Import of the class Movement and add of the first two functions

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""