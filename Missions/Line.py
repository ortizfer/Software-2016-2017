# Line Mission
from Missions import Movement
from Utils import Log
from Vision import FrameGrab, messPassing, PathPCA2, FrameGrabRT
import time
'''
Line Mission Logic. The file aims to align the AUV to the direction of the mission.
'''

'''
************************************************************************************************************************
Dictionary:
--Function--
start(): essentially the main function of the file. Completes the line mission by aligning with the line.
    parameter: void
    return: void
************************************************************************************************************************
'''
# Start Line mission logic


def start():

    print("Starting Line mission")
    Log.Logging.logSys("Line.py: Starting Line mission")

    aligned = False
    FrameGrabRT.startLive()
    # Find the direction we want to go (obtain direction object)
    #while direction.angle == -1:
     #   direction = Movement.get_direction()

    # Align AUV with line
    while not aligned:
        print("aligning with line")
        Log.Logging.logSys("Line.py: Aligning with line")
        #Picture of floor
        FrameGrab.floorFrame()
        #Angle of path
        message = messPassing.messPassing()
        message = PathPCA2.startPathPCA()
        found = message.impFound()

        # AUV is aligned if 10 > Angle > -10
        print(message.impAngle())

        while message.impAngle() > 10 or message.impAngle() < -10:
            if message.impAngle() > 10:
                Movement.align('-8')
                time.sleep(2)

            if message.impAngle() < -10:
                Movement.align('8')
                time.sleep(2)

            FrameGrab.floorFrame()
            message = PathPCA2.startPathPCA()
        aligned = True

    # Move in aligned direction 40%
    if aligned:
        Movement.forward(9)

    print("Exiting Line")
    Log.Logging.logSys("Line.py: Exiting Line")


"""
VERSION CONTROL:

6- Fernando Ortiz 25/5/2017 12:00 PM
Updated Line code with vision logic

5- Juan G. Lastra Febles 10/05/2017 7:13 PM
Documented the code

4-  Carlos J. Figueroa 01/03/2017 11:18pm
Added calls to System Log.

3- Fernando Ortiz 20/02/17
Implementation of Line mission logic

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""