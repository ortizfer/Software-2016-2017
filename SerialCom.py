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

"""
VERSION CONTROL:

4- Carlos J. Figueroa 23/02/2017 4:26pm
Added basic documentation.

3- Fernando Ortiz 20/02/17
Implementation of Serial Communications

1- Fernando Ortiz 20/02/17
Initial Commit and creation of class.

"""