# Gate 2 Mission
import Movement


# Start Gate2 mission logic
def start():

    found_gate = False
    aligned = False
    print("Starting Gate2 mission")

    while not found_gate:
        print("Searching for gate")
        found_gate = True
    while not aligned:
        print("Aligning with gate")
        aligned = True

    # Move forward 40%
    Movement.forward(10)

    # Do movement trick for gate
    Movement.do_magic()

    print("Exiting Gate2 mission")


"""
VERSION CONTROL:

2- Fernando Ortiz 21/02/17
Initial implementation of Gate2 mission logic

1- Fernando Ortiz 17/02/17
Initial Commit and creation of class.

"""