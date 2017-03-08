# Buoy Mission
from Missions import Movement

'''
    The Buoy mission commences by  searching for  buoy's. The
    buoys'  general  direction  is given by the  orange  line
    marker. Once the buoys are detected, the sub will attempt
    to bop the  red buoy, then  the green.  After both  buoys
    have been touched,  the sub  will try to navigate between
    them to begin searching for the next orange line marker.
'''

# noinspection PyPep8Naming
# ^^^ Suppresses spelling warnings on camel-cased  variables.


def start():
    _maxrangex= 500
    _maxrangey= 300

    redBuoy = True

    direction = Movement.get_direction()

    aligned = False
    # Starting Buoy mission
    print("Starting Buoy mission")

    while direction.angle == 0:
        direction = Movement.get_direction()

    while not aligned:
        print("aligning with redBuoy")
        aligned = True

    # move 10 feet then touch the Buoy
    if aligned:

        Movement.forward(10)
        Movement.bop_it()
        Movement.backward()

    greenBuoy = True
    redBuoy = False
    # aligning with green Buoy

    if greenBuoy:

        direction = Movement.get_direction()

        aligned = False

    while direction.angle == 0:
        direction = Movement.get_direction()

    while not aligned:
        print("aligning with greenBuoy")
        aligned = True

    if aligned:
        Movement.forward(10)
        Movement.bop_it()
        Movement.backward()

# Exit algorithm
    Movement.forward(5)

    print("Exiting Buoy mission")


"""
VERSION CONTROL:
13- Sachy Romero 27/02/2017 12:28pm
Added Maxrange X and Maxrange Y

12- Carlos J. Figueroa 23/02/2017 5:01pm
Added basic documentation. Added a naming convention suppressant(line 14).

11- Sachy Romero 22/02/2017
Exit algorithm and pass between the Buoys

10- Sachy Romero 22/02/2017
Touch Green Buoy

9- Sachy Romero 22/02/2017
Aligned with Green Buoy

7- Sachy Romero 22/02/2017
Moved backward to align with green Buoy

6- Sachy Romero Rosado 22/02/2017
Touch Red Buoy

5- Sachy Romero 22/02/2017
Aligned to Red Buoy

4- Sachy Romero 21/02/17
Added boolean variable for Buoy mission

3- Fernando Ortiz 20/02/17
Added debugging prints

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""
