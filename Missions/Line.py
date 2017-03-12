# Line Mission
from Missions import Movement
from Utils import Log


# Start Line mission logic
def start():

    print("Starting Line mission")
    Log.Logging.logSys("Line.py: Starting Line mission")

    aligned = False

    direction = Movement.get_direction()

    # Find the direction we want to go (obtain direction object)
    while direction.angle == -1:
        direction = Movement.get_direction()

    # Align AUV with direction
    while not aligned:
        print("aligning with line")
        Log.Logging.logSys("Line.py: Aligning with line")
        aligned = True

    # Move in aligned direction 40%
    if aligned:
        Movement.forward(10)

    print("Exiting Line")
    Log.Logging.logSys("Line.py: Exiting Line")


"""
VERSION CONTROL:
4-  Carlos J. Figueroa 01/03/2017 11:18pm
Added calls to System Log.

3- Fernando Ortiz 20/02/17
Implementation of Line mission logic

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""