# Line Mission
import Movement

# Start Line mission logic
def start():

    print("Starting Line mission")
    aligned = False

    direction = Movement.get_direction()

    # Find the direction we want to go (obtain direction object)
    while direction.angle == -1:
        direction = Movement.get_direction()

    # Align AUV with direction
    while not aligned:
        print("aligning with line")
        aligned = True

    # Move in aligned direction 40%
    if aligned:
        Movement.forward(10)

    print("Exiting Line")



"""
VERSION CONTROL:

3- Fernando Ortiz 20/02/17
Implementation of Line mission logic

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""