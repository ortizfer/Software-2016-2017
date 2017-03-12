from Utils import Timer

'''
    DOCUMENTATION NEEDED
'''


# noinspection PyPep8Naming
class Logging:

    __NavFile = open("..\\Logs\\dummy", "w")
    __ErrFile = open("..\\Logs\\dummy", "w")
    __SysFile = open("..\\Logs\\dummy", "w")
    __currDate = Timer.Timer().currDateTime()
    __navName = "NavLog_"
    __errName = "ErrLog_"
    __sysName = "SysLog_"

    # Initializes the files for the current. MUST be called calling any other function.
    @staticmethod
    def createLogs():
        # Creating necessary data

        Logging.__currDate = Timer.Timer().currDateTime()
        extension = ".txt"
        directory = "..\\Logs\\"

        # Creating file names

        Logging.__navName = directory + "NavLog_" + Logging.__currDate + extension
        Logging.__errName = directory + "ErrLog_" + Logging.__currDate + extension
        Logging.__sysName = directory + "SysLog_" + Logging.__currDate + extension

        # Creating files
        mode = "w"
        Logging.__NavFile = open(Logging.__navName, mode)
        Logging.__ErrFile = open(Logging.__errName, mode)
        Logging.__SysFile = open(Logging.__sysName, mode)

        # Adding names as header
        Logging.logNav(Logging.__navName+"\n")
        Logging.logErr(Logging.__errName+"\n")
        Logging.logSys(Logging.__sysName+"\n")

        Logging.__closeLogs()

    # Writes a new line to the Navigation Log
    @staticmethod
    def logNav(message):
        Logging.__openNav()
        Logging.__NavFile.seek(0, 2)
        Logging.__NavFile.write(message + ": " + Timer.Timer().formattedDateTime() + "\n")
        Logging.__closeNav()

    # Writes a new line to the Error Log
    @staticmethod
    def logErr(message):
        Logging.__openErr()
        Logging.__ErrFile.seek(0, 2)
        Logging.__ErrFile.write(message + ": " + Timer.Timer().formattedDateTime() + "\n")
        Logging.__closeErr()

    # Writes a new line to the System Log
    @staticmethod
    def logSys(message):
        Logging.__openSys()
        # Logging.__SysFile.seek(0, 2)
        Logging.__SysFile.write(message + ": " + Timer.Timer().formattedDateTime() + "\n")
        Logging.__closeSys()

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
4- Carlos J. Figueroa 11/03/2017 9:14pm
Modified the write functions to use the formattedDateTime from Timer.py.

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



