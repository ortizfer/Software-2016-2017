import Gate1
import Line
import Buoy
import Gate2
import Island

firstRun = True

print("starting Process")
Gate1.start()

Line.start()

if firstRun:

    firstRun = False

    Buoy.start()

    Line.start()

if not firstRun:

    Gate2.start()

    Island.start()

print("Finished")


"""
VERSION CONTROL:

3- Fernando Ortiz 20/02/17
Main implementation of all missions

2- Fernando Ortiz 19/02/17
Main class to run all missions

1- Fernando Ortiz 19/02/17
Initial Commit and creation of class.

"""