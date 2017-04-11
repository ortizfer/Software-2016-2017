# Line Mission
from Missions import Movement
from Utils import Log, SerialCom
from Vision import FrameGrab, AngleTest



# Start Line mission logic
def start():

    print("Starting Line mission")
    Log.Logging.logSys("Line.py: Starting Line mission")

    aligned = False

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
        Angle = AngleTest.sendPath()

        # AUV is aligned if 10 > Angle > -10
        if Angle > 10 or Angle < -10:
            # Angle is valid for alignment if is under 360 degree
            if not Angle > 360:
                #print("Aligning")
                Movement.align(Angle)
        else :
            aligned = True

    # Move in aligned direction 40%
    if aligned:
        Movement.forward(9)

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