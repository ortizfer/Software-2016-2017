README for Depth Controller Smapling Betav0.1
Author: Jose A. Montes Perez	Date: 16-02-17
*************************************************************
This Readme contains instructions from wiring to sending 
commands to the msp 430 interface and the Razor IMU. 

*************************************************************
MSP430
*************************************************************
Step 1. Wiring

The msp430 MCU is connected both to the host pc that sends
commands (laptop or raspberry pi), and to the PWM controlled
ESC motor drivers. 

Pc Connection
You connect it to the PC via USB. If you are on a windows
machine you have to verify the COM port that it registers in,
it will appear as msp430 UART application. The device serial
port configuration has to be set up as 9600 baud, 8n1 with 
no hardware flow control. You can use a program like PuTTy
to connect to the msp using theese settings. 

The raspberry pi is configured to use minicom terminal. 
Simply tipe minicom at the terminal pompt and you will
conect to the msp430.

However if you are on a linux machine you must use a terminal
application like minicom. Check the /dev directory to verify 
the name of the device, it is usually /dev/ttyACM1. If you 
cannot identify it just unplug it and look for any difference, 
that is the msp430. With this you can configure a terminal 
application using the port settings described above.

Motor Controllers
To connect the motor controllers you must identify which
ones are vertical and horizontal. The signal pin for the
vertical motors go in the pins 2.5-2.4. The horizontal 
motors are connected to the pins 1.5-1.2.

Step 2.
MSP430 Commands
The following are the commands that the current firmware 
supports:

x - Cuts of power to the motors by setting it in the 
    deadband.

w - Increase speed of horizontal thrusters by 5%,
    doesnt take into consideration the motor cap.
    If the motor is turning, it will set the speed
    to 0 and then increase the speed.
s - Decreases speed of horizontal thrusters by 5%,
    doesnt take into consideration the motor cap.
    If the motor is turning, it will set the speed
    to 0 and then increase the speed.
a - Increases the speed of the right motor by 5%
    and decreases the speed of the left motor by 5%.
    Doesnt scale with motor cap.
    If the motors are going forwards or backwards it
    sets the speed to zero then it changes the speed.
d - Decreases the speed of the right motor by 5%
    and increases the speed of the left motor by 5%.
    Doesnt scale with the motor cap.
    If the motors are going forwards or backwards it
    sets the speed to zero then it changes the speed.

o - Increases 5% to the horizontal motors. Doesnt scale
    with motor cap.
l - Decreases 5% to the horizontal motors. Doesnt scale
    with motor cap.

t - toggles the motors which the '1'-'0' commands apply
    to.

1 - sends 10% (scaled to the motor cap) to the motors
    pointed by t.
2 - sends 20% (scaled to the motor cap) to the motors
    pointed by t
3 - sends 30% (scaled to the motor cap) to the motors
    pointed by t.
4 - sends 40% (scaled to the motor cap) to the motors
    pointed by t.
5 - sends 50% (scaled to the motor cap) to the motors
    pointed by t.
6 - sends 60% (scaled to the motor cap) to the motors
    pointed by t.
7 - sends 70% (scaled to the motor cap) to the motors
    pointed by t.
8 - sends 80% (scaled to the motor cap) to the motors
    pointed by t.
9 - sends 90% (scaled to the motor cap) to the motors
    pointed by t.
0 - sends 100% (scaled to the motor cap) to the motors
    pointed by t.






 - For Friday - 
Step 1. Connect pc to ethernet
Step 2. Open ssh client (putty o terminal)
Step 3. Login to pi ip = 169.254.0.2 , user: pi, password: raspberry
If (want = control motors){
    Step 4. type "minicom" and press enter. NOTE: PRESS X OR MOTORS WILL START AUTOMATICALLY
    Step 5. Send commands by typping the keys.
    If (want = capture pressure){
        Step 6. Press "ctrl + A" to enter control mode
        Step 7. Press 'l' to begin capture
	Step 8. Write (proper) name and press enter (.csv) (.txt)
	Step 9. jump to step 5

To stop presure measurements 
"ctrl + A" to enter control mode
Press 'l' to begin capture
Press " exit "

Press 
    }
    If (want = exit){
	Step 10. Press " X "  to stop motors
	Step 11. Press "ctrl + A" for control mode
	Step 12. Press " X " 
	Step 13. Press " Yes "
    }
} 
If(want = readIMU){
	Step 14. Write "./readimu.sh &"
	
}

	Step 15. Write "minicom" : Press X to stop motors
	Step 16. Jump to Step 5.


	
	







