import serial

'''
Establishes a connection with tty0 and tty1. Both these
represent two way communication with the USB ports.
'''


# Creates two serial objects to communicate with the USB ports.
try:
    ser1 = serial.Serial("/dev/ttyACM1", 9600)
except:
    pass

try:
    ser0 = serial.Serial("/dev/ttyACM0", 9600)
except:
    pass

'''
# Listens to port 0
def read0():
    ser0.readline()


# Listens to port 1
def read1():
    ser1.readline()


# Sends to port 0
def write0(command):
    ser0.write(command)


# Sends to port 1
def write1(command):
    ser1.write(command)
'''


def readMSPFRONT():
    return ser0.readLine()


def writeMSPFRONT(command):
    ser0.write(command)


def readMSPUP():
    return ser0.readLine()


def writeMSPUP(command):
    ser0.write(command)


def readDSPIC():
    return ser0.readLine()


def writeDSPIC(command):
    ser0.write(command)


def readPSENSE():
    return ser0.readLine()

def writePSENSE(command):
    ser0.write(command)

def readIMU():
    return ser0.readLine()

def writeIMU(command):
    ser0.write(command)


"""
VERSION CONTROL:

6- Carlos J. Figueroa 01/03/2017 6:46pm
Added write commands for IMU and PSENSE.

5- Carlos J. Figueroa 28/02/2017 11:10am
Commented generic read/write commands. Added read commands for
MSPUP, MSPFRONT, PSENSE, IMU, and DSPIC.  Added write commands
for MSPFRONT, MSPUP, and DSPIC.

4- Carlos J. Figueroa 23/02/2017 4:26pm
Added basic documentation.

3- Fernando Ortiz 20/02/17
Implementation of Serial Communications

1- Fernando Ortiz 20/02/17
Initial Commit and creation of class.

"""