import Timer
import Log

'''
    DOCUMENTATION NEEDED
'''

mode = "w"
__NavFile = open("Logs/dummy1", mode)
__ErrFile = open("Logs/dummy2", mode)
__SysFile = open("Logs/dummy3", mode)


# noinspection PyPep8Naming

# Initializes the files for the current. MUST be called calling any other function.
def createLogs():
    # Creating necessary data
    currDate = Timer.Timer().currDateTime()
    extension = ".txt"

    # Creating file names
    navName = "Logs/NavLog_" + currDate + extension
    errName = "Logs/ErrLog_" + currDate + extension
    sysName = "Logs/SysLog_" + currDate + extension

    # Creating files
    Log.__NavFile.close()
    Log.__ErrFile.close()
    Log.__SysFile.close()

    Log.__NavFile = open(navName, mode)
    Log.__ErrFile = open(errName, mode)
    Log.__SysFile = open(sysName, mode)

    # Adding names as header
    logNav(navName+"\n")
    logErr(errName+"\n")
    logSys(sysName+"\n")


# Writes a new line to the Navigation Log
def logNav(message):
    __NavFile.write(message + ": " + Timer.Timer().currDateTime())


# Writes a new line to the Error Log
def logErr(message):
    __ErrFile.write(message + ": " + Timer.Timer().currDateTime())


# Writes a new line to the System Log
def logSys(message):
    __SysFile.write(message + ": " + Timer.Timer().currDateTime())


# Closes all files
def closeLogs():
    __NavFile.close()
    __ErrFile.close()
    __SysFile.close()


'''
VERSION CONTROL:
2-  Carlos J. Figueroa 01/03/2017 11:15pm
Added DateTime to log functions.

1- Carlos J. Figueroa 01/03/2017 10:42pm
Initial Commit:
Implemented general Log.py file. Created three file variables with dummy values.
Added methods createLogs(), logNav(), logErr(), logSys(), and closeLogs().
Imported Timer.
'''



