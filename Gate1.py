# Gate1 Mision

import Movement
import time
import Log


# start mission logic
def start():

    position = Movement.get_depth()

    print("Starting Gate1 mission")
    Log.logSys("Gate1.py: Starting Gate1 mission")
    # Submerge the AUV to 4 feet
    Movement.submerge("4")
    time.sleep(4)
    while position > 5 or position < 3:
        if position > 5:

            Movement.surface("x")
            time.sleep(4)

        elif position < 3:

            Movement.submerge("x")
            time.sleep(4)
        position = Movement.get_depth()

    # Full 40% forward
    Movement.forward(10)
    # stop AUV
    Movement.stop()
    print("exiting Gate1")
    Log.logSys("Gate1.py: exiting Gate1")


"""
VERSION CONTROL:
4- Carlos J. Figueroa 01/03/2017 11:20pm
Added calls to System Log.

3- Fernando Ortiz 20/02/17
Finished implementation on Gate1 logic

2- Fernando Ortiz 19/02/17
Import of the class Movement and add of the first two functions

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""