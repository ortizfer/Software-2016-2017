To write command to MSP430:

echo command > /dev/ttyACM1
or
echo command > /dev/ttyACM0

Command List:
w - front motors + 5%
s - front motors - 5%
a - front motors turn + 5%
d - front motors turn - 5%

o - vert motors + 5%
l - vert motors - 5%

x - kill motors

1 - 10% all motors
2 - 20% all motors
3
|  Same behaviour
0


To read from MSP430

To screen 
cat /dev/ttyACM0

To file 
timeout 60 cat /dev/ttyACM0 > pressure_reading.csv &

To read from IMU

To screen
cat /dev/ttyUSB0

To file
timeout 60 cat /dev/ttyUSB0 > imu_reading.csv &
