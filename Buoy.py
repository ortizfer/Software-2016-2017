# Buoy Mission
import Movement

def start():
    redBuoy = True

    direction = Movement.get_direction()

    aligned = False
    # Starting Buoy mission
    print("Starting Buoy mission")

    while direction.angle== 0:
        direction = Movement.get_direction()

    while not aligned:
        print("aligning with redBuoy")
        aligned = True

    # move 10 feet then touch the Buoy
    if aligned:

        Movement.forward(10)
        Movement.bop_it()
        Movement.backward()

    greenBuoy= True
    redBuoy= False
    # aligning with green Buoy

    if greenBuoy:

        direction = Movement.get_direction()

        aligned = False

    while direction.angle== 0:
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
