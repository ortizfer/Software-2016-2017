from abc import ABCMeta
import time

'''
    When Timer is initialized it stores the current time as start time.
    Calling resetTimer sets the startTime to the current time.
    Calling endTimer takes the current time, stores it, and calculates the
    difference between endTime and startTime.
'''

# noinspection PyPep8Naming
class Timer:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.startTime = time.time()

    def resetTimer(self):
        self.startTime = time.time()
        return self.startTime

    def endTimer(self):
        return time.time() - self.startTime

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def getTimeSpent(self):
        return self.timeSpent


'''
VERSION CONTROL:

2- Carlos J. Figueroa 2/22/2017 4:29pm
    Removed redundant functions and properties.

1- Carlos J. Figueroa 2/22/2017 4:15pm
    Initial commit, with original version of timer.
'''