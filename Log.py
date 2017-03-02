from Timer import *

'''
    DOCUMENTATION NEEDED
'''

__NavFile = file("")
__ErrFile = file("")
__SysFile = file("")


# noinspection PyPep8Naming

# Initializes the files for the current. MUST be called calling any other function.
def createLogs():
    # Creating necessary data
    currDate = str(Timer.currDateTime())
    extension = ".txt"
    mode = "w"

    # Creating file names
    navName = "NavLog_" + currDate + extension
    errName = "ErrLog_" + currDate + extension
    sysName = "SysLog_" + currDate + extension

    # Creating files
    __NavFile = open(navName, mode)
    __ErrFile = open(errName, mode)
    __SysFile = open(sysName, mode)

    # Adding names as header
    logNav(navName+"\n")
    logErr(errName+"\n")
    logSys(sysName+"\n")


# Writes a new line to the Navigation Log
def logNav(message):
    __NavFile.write(message)


# Writes a new line to the Error Log
def logErr(message):
    __ErrFile.write(message)


# Writes a new line to the System Log
def logSys(message):
    __SysFile.write(message)


# Closes all files
def closeLogs():
    __NavFile.close()
    __ErrFile.close()
    __SysFile.close()


'''
VERSION CONTROL:

1- Carlos J. Figueroa 01/03/2017 10:42pm
Initial Commit:
Implemented general Log.py file. Created three file variables with dummy values.
Added methods createLogs(), logNav(), logErr(), logSys(), and closeLogs().
Imported Timer.
'''



