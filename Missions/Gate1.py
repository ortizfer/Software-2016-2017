# Gate1 Mission

import time
from Missions import Movement
from Utils import Log
'''
Gate1 Mission Logic. This file aims to complete the Gate1 mission which is to pass the first gate of the competition
'''

'''
************************************************************************************************************************
Dictionary:
--Function--
start(): essentially the main function of the file. Completes the Gate1 mission by moving forward.
    parameter: void
    return: void

************************************************************************************************************************
'''
# start mission logic
def start():

    print("Starting Gate1 mission")
    Log.Logging.logSys("Gate1.py: Starting Gate1 mission")
    # Submerge the AUV to 6 feet
    Movement.depth("6")
    time.sleep(4)

    # Full 40% forward
    Movement.forward(9)

    print("Exiting Gate1")
    Log.Logging.logSys("Gate1.py: exiting Gate1")


"""
VERSION CONTROL:
7- Juan G. Lastra Febles and Carlos Figueroa 10/05/2017 6:46 PM
Edited the documentatio

6- Sachy Romero 02/04/2017 1:32
Changed the feet on deph from 4 to 6 feet

5- Sachy Romero 02/04/2017  1:32am
Deleted unnecessary code to leave the log implementation

4- Carlos J. Figueroa 01/03/2017 11:20pm
Added calls to System Log.

3- Fernando Ortiz 20/02/17
Finished implementation on Gate1 logic

2- Fernando Ortiz 19/02/17
Import of the class Movement and add of the first two functions

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""