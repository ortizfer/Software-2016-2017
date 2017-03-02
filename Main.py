import Log
import Gate1
import Line
import Buoy
import Gate2
import Island


'''
Main Mission Logic.  Establishes  order of missions and calls each
one correspondingly. Currently performed missions are: Gate1, Line
Buoy, Line (again), Gate2, and Island.

At the start, the  submarine submerges itself and moves forward to
cross the first Gate. Next it aligns itself with the orange marker
and moves forward until it detect the buoys. After  finishing  the
buoy mission the submarine aligns itself with the last line marker
and moves to find the second gate. Crossing the gate  the sub  can
attempt  to  perform a stunt. Finally the  submarine  locates  the
Island octagon with the hydrophones and surfaces.
'''

Log.createLogs()

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

5- Carlos J. Figueroa 01/03/2017 10:49pm
Imported Log.py and added line to create logs.

4- Carlos J. Figueroa 23/02/2017 4:41pm
Added some basic documentation.

3- Fernando Ortiz 20/02/17
Main implementation of all missions

2- Fernando Ortiz 19/02/17
Main class to run all missions

1- Fernando Ortiz 19/02/17
Initial Commit and creation of class.

"""