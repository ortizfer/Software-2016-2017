import serial

try:
    ser1 = serial.Serial("/dev/ttyACM1", 9600)
except:
    pass

try:
    ser0 = serial.Serial("/dev/ttyACM0", 9600)
except:
    pass


def read0():
    ser0.readline()


def read1():
    ser1.readline()


def write0(command):
    ser0.write(command)


def write1(command):
    ser1.write(command)

"""
VERSION CONTROL:

3- Fernando Ortiz 20/02/17
Implementation of Serial Communications

1- Fernando Ortiz 20/02/17
Initial Commit and creation of class.

"""