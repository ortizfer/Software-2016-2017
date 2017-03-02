import datetime
import time

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

    def currDateTime(self):
        d = datetime.datetime.now()
        formattedDate = str(
            "Y" + str(d.year) +
            "M" + str(d.month) +
            "D" + str(d.day) +
            "_H" + str(d.hour) +
            "M" + str(d.minute) +
            "S" + str(d.second)
        )
        return formattedDate


'''
VERSION CONTROL:
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