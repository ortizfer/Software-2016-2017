# Gate 2 Mission
import Movement
import Log

# Start Gate2 mission logic
def start():

    found_gate = False
    aligned = False
    print("Starting Gate2 mission")
    Log.logSys("Gate2.py: Starting Gate2 mission")

    while not found_gate:
        print("Searching for gate")
        Log.logSys("Gate2.py: Searching for gate")
        found_gate = True
    while not aligned:
        print("Aligning with gate")
        Log.logSys("Gate2.py: Aligning with gate")
        aligned = True

    # Move forward 40%
    Movement.forward(10)

    # Do movement trick for gate
    Movement.do_magic(4)

    print("Exiting Gate2 mission")
    Log.logSys("Gate2.py: Exiting Gate2 mission")


"""
VERSION CONTROL:
3- Carlos J. Figueroa 01/03/2017 11:23pm
Added calls to System Log.

2- Fernando Ortiz 21/02/17
Initial implementation of Gate2 mission logic

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""