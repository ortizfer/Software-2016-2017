# Gate 2 Mission
from Missions import Movement
from Utils import Log
'''
Gate 2 Mission Logic. This file aims to complete Gate2 mission where te AUV must pass through a gate and
perform a stunt.
'''

'''
************************************************************************************************************************
Dictionary:
--Functions--
start(): essentially the main function of the file, passes the gate obstacle by moving forward and performing a stunt.
    parameter: void
    return: void

************************************************************************************************************************
'''

# Start Gate2 mission logic
def start():

    found_gate = False
    aligned = False
    print("Starting Gate2 mission")
    Log.Logging.logSys("Gate2.py: Starting Gate2 mission")

    while not found_gate:
        print("Searching for gate")
        Log.Logging.logSys("Gate2.py: Searching for gate")
        found_gate = True
    while not aligned:
        print("Aligning with gate")
        Log.Logging.logSys("Gate2.py: Aligning with gate")
        aligned = True

    # Move forward 40%
    Movement.forward(10)

    # Do movement trick for gate
    Movement.align(180)
    Movement.backward(1)

    print("Exiting Gate2 mission")
    Log.Logging.logSys("Gate2.py: Exiting Gate2 mission")


"""
VERSION CONTROL:
4- Juan G. Lastra Febles and Carlos Figueroa 10/05/2017 6:50 PM
Edited the documentation

3- Carlos J. Figueroa 01/03/2017 11:23pm
Added calls to System Log.

2- Fernando Ortiz 21/02/17
Initial implementation of Gate2 mission logic

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""