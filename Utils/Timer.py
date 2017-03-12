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
            "Y_" + str(d.year) +
            "_M_" + str(d.month) +
            "_D_" + str(d.day) +
            "_H_" + str(d.hour) +
            "_M_" + str(d.minute) +
            "_S_" + str(d.second)
        )
        return formattedDate

    def formattedDateTime(self):
        d = datetime.datetime.now()
        a = [
            str(d.day),
            str(d.month),
            str(d.year),
            str(d.hour),
            str(d.minute),
            str(d.second)
        ]
        for i in range(0, len(a)):
            if len(a[i]) < 2:
                string = "0"
                string = str(string + a[i])
                a[i] = string

        formattedDate = str(
            a[0]+"/"+
            a[1]+"/"+
            a[2]+"_"+
            a[3]+":"+
            a[4]+":"+
            a[5]
        )
        return formattedDate

'''
VERSION CONTROL:
6- Carlos J. Figueroa 11/03/2017 9:14pm
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