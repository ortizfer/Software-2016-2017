import datetime
import time
from Utils import StringOperations

'''
    When Timer is initialized it stores the current time as self.startTime.
    Calling resetTimer sets the startTime to the current time and returns it.
    Calling endTimer takes the current time, and calculates the difference.
'''


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Timer:
    def __init__(self):
        self.startTime = time.time()

    def resetTimer(self):
        self.startTime = time.time()
        return self.startTime

    def endTimer(self):
        return time.time() - self.startTime

    def getStartTime(self):
        return self.startTime


# Reformats the given datetime object into a string for use in Log file names
def FileDateTime(timenow):
    d = timenow
    formattedDate = str(
        "Y_" + str(d.year) +
        "_M_" + str(d.month) +
        "_D_" + str(d.day) +
        "_H_" + str(d.hour) +
        "_M_" + str(d.minute) +
        "_S_" + str(d.second)
    )
    return formattedDate


# Reformats the given datetime object into a string for writing into the logs
def LogDateTime(timenow):
    d = timenow
    a = [
        str(d.day),
        str(d.month),
        str(d.year),
        str(d.hour),
        str(d.minute),
        str(d.second)
    ]
    for i in range(0, len(a)):
        a[i] = StringOperations.extendString(a[i], '0', 2, 0)

    formattedDate = str(
        a[0]+"/"+
        a[1]+"/"+
        a[2]+"_"+
        a[3]+":"+
        a[4]+":"+
        a[5]
    )
    return formattedDate


# Returns the the current time in datetime format
def getTime():
    return datetime.datetime.now()

'''
VERSION CONTROL:
7- Carlos J. Figueroa 01/04/2017 2:38pm
Added function getTime. Renamed currDateTime to FileDateTime.
Renamed formattedDateTime to LogDateTime. Both functions now
take an object of type datetime and formats it to each speci
fication.

6- Carlos J. Figueroa 11/03/2017 9:17pm
Added formatted time for log entries.

5- Carlos J. Figueroa 11/03/2017 8:46pm
Changed format of currDate.

4- Carlos J. Figueroa 01/03/2017 11:35pm
Modified previous VC entries with proper date format.
Imported datetime; added currDateTime function.

3- Carlos J. Figueroa 22/02/2017 4:39pm
Updated documentation, removed meta class declaration.

2- Carlos J. Figueroa 22/02/2017 4:29pm
Removed redundant functions and properties.

1- Carlos J. Figueroa 22/02/2017 4:15pm
Initial commit, with original version of timer.
'''