from Utils import Timer
from Utils import StringOperations
from GUI import v3

'''
    DOCUMENTATION NEEDED
'''


# noinspection PyPep8Naming

# These program is to put the information and writes it to a log file
class Logging:

    # Pointers to the corresponding Log files
    __NavFile = open("../Logs/dummy", "w")
    __ErrFile = open("../Logs/dummy", "w")
    __SysFile = open("../Logs/dummy", "w")

    # Strings corresponding the Log names
    __navName = "NavLog_"
    __errName = "ErrLog_"
    __sysName = "SysLog_"

    # Current datetime
    __currDate = Timer.getTime()

    # Amount of characters per log entry, excluding timestamp
    __correction = 20

    # Character used as spacer in log entries
    __spacer = '.'

    # Initializes the files for the current. MUST be called before calling any other function.
    @staticmethod
    def createLogs():
        # Creating necessary data

        Logging.__currDate = Timer.getTime()
        extension = ".txt"
        directory = "../Logs/"
        headerDecals = "-=-=-=-=-=-=-=-=-=-=-=-"

        # Creating file names

        Logging.__navName = directory + "NavLog_" + Timer.FileDateTime(Logging.__currDate) + extension
        Logging.__errName = directory + "ErrLog_" + Timer.FileDateTime(Logging.__currDate) + extension
        Logging.__sysName = directory + "SysLog_" + Timer.FileDateTime(Logging.__currDate) + extension

        # Creating files
        mode = "w"
        Logging.__NavFile = open(Logging.__navName, mode)
        Logging.__ErrFile = open(Logging.__errName, mode)
        Logging.__SysFile = open(Logging.__sysName, mode)

        # Adding names as header
        Logging.logNav(headerDecals + Logging.__navName + headerDecals + "\n")
        Logging.logErr(headerDecals + Logging.__errName + headerDecals + "\n")
        Logging.logSys(headerDecals + Logging.__sysName + headerDecals + "\n")

        Logging.__closeLogs()

    # Writes a new line to the Navigation Log
    @staticmethod
    def logNav(message):
        Logging.__openNav()
        Logging.__NavFile.write(
            StringOperations.extendString(message, Logging.__spacer, Logging.__correction, 1) +
            Timer.LogDateTime(Timer.getTime()) + "\n")
        Logging.__closeNav()
        v3.sendMessage(message)
        print(message)

    # Writes a new line to the Error Log
    @staticmethod
    def logErr(message):
        Logging.__openErr()
        Logging.__ErrFile.write(
            StringOperations.extendString(message, Logging.__spacer, Logging.__correction, 1) +
            Timer.LogDateTime(Timer.getTime()) + "\n")
        Logging.__closeErr()
        v3.sendMessage(message)
        print(message)

    # Writes a new line to the System Log
    @staticmethod
    def logSys(message):
        Logging.__openSys()
        Logging.__SysFile.write(
            StringOperations.extendString(message, Logging.__spacer, Logging.__correction, 1) +
            Timer.LogDateTime(Timer.getTime()) + "\n")
        Logging.__closeSys()
        v3.sendMessage(message)
        print(message)

    # Closes all files
    @staticmethod
    def __closeLogs():
        Logging.__NavFile.close()
        Logging.__ErrFile.close()
        Logging.__SysFile.close()

    @staticmethod
    def __openNav():
        Logging.__NavFile = open(Logging.__navName, "a")

    @staticmethod
    def __closeNav():
        Logging.__NavFile.close()

    @staticmethod
    def __openErr():
        Logging.__ErrFile = open(Logging.__errName, "a")

    @staticmethod
    def __closeErr():
        Logging.__ErrFile.close()

    @staticmethod
    def __openSys():
        Logging.__SysFile = open(Logging.__sysName, "a")

    @staticmethod
    def __closeSys():
        Logging.__SysFile.close()


'''
VERSION CONTROL:
7- Carlos J. Figueroa 01/04/2017 3:18pm
Added decals to Log headers. Modified each logs write function
to use correct to 10 characters per message, excluding the
timestamp. Currently uses '.' as the spacer. this can be
configured.

6- Fernando Ortiz 14/02/2017
Fixed path for windows and mac systems

5- Juan G. Lastra Febles 14/03/2017
Add a documentation in the program and put a print function to the log functions

4- Carlos J. Figueroa 11/03/2017 9:14pm
Modified write functions to use the formattedDateTime from Timer.py.

3- Carlos J. Figueroa 11/03/2017 8:46pm
Log correctly functioning. Added methods and variables within a class.
Modified methods to work statically.

2-  Carlos J. Figueroa 01/03/2017 11:15pm
Added DateTime to log functions.

1- Carlos J. Figueroa 01/03/2017 10:42pm
Initial Commit:
Implemented general Log.py file. Created three file variables with dummy values.
Added methods createLogs(), logNav(), logErr(), logSys(), and closeLogs().
Imported Timer.
'''



