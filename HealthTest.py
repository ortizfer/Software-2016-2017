import SerialCom

'''
    The HealthTest.py file  contains the method HealthTest()
    and an Exception  class,  HealthException.  HealthTest()
    runs diagnostics on the sub's system's, if it not ready
    for a run it will raise the HealthException.
'''


# noinspection PyPep8Naming
def healthTest():
    hCall = "HEALTH"  # health call; string to be sent
    xReply = "OK"     # expected reply

    # Each variable holds a True or False value depending on the systems diagnostics
    MSPFRONT = __healthMSPFRONT(hCall, xReply)
    MSPUP = __healthMSPUP(hCall, xReply)
    PSENSE = __healthPSENSE(hCall, xReply)
    IMU = __healthIMU(hCall, xReply)
    DSPIC = __healthDSPIC(hCall, xReply)

    ready = MSPFRONT and MSPUP and PSENSE and IMU and DSPIC

    if not ready:
        # passes dictionary as the exception message
        error = {"MSPFRONT": MSPFRONT, "MSPUP": MSPUP, "PSENSE": PSENSE, "IMU": IMU, "DSPIC": DSPIC}
        raise HealthException(str(error))

    else:
        return ready


# Private Functions for performing diagnostics on individual systems
def __healthMSPFRONT(call, reply):
    SerialCom.writeMSPFRONT(call)
    return SerialCom.readMSPFRONT() == reply


def __healthMSPUP(call, reply):
    SerialCom.writeMSPUP(call)
    return SerialCom.readMSPUP() == reply


def __healthDSPIC(call, reply):
    SerialCom.writeDSPIC(call)
    return SerialCom.readDSPIC() == reply


def __healthPSENSE(call, reply):
    SerialCom.writePSENSE(call)
    return SerialCom.readPSENSE() == reply


def __healthIMU(call, reply):
    SerialCom.writeIMU(call)
    return SerialCom.readIMU() == reply


# Raised if diagnostics detects an error
class HealthException(Exception):
    pass

'''
VERSION CONTROL:
2- Carlos J. Figueroa 01/03/2017 6:47pm
Modified IMU and PSENSE to send "HEALTH" and expect "OK"

1- Carlos J. Figueroa 28/02/2017 11:56am
Original  implementation and file creation. Includes
the public  function healthTest(),  multiple private
functions for diagnostics, and class HealthException.
'''
