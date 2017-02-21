# Line Mission
import Movement


def start():
    print("Starting Line mission")
    aligned = False
    direction = Movement.get_direction()
    while direction.angle == -1:
        direction = Movement.get_direction()

    while not aligned:
        print("aligning with line")
        aligned = True

    if aligned:
        Movement.forward(10)

    print("Exiting Line")

if __name__ == '__main__':
    print()

"""
VERSION CONTROL:

3- Fernando Ortiz 20/02/17
Implementation of Line mission logic

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""