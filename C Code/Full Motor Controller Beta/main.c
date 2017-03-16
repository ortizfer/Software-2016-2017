#include <msp430.h> 
#include "Motors_JMP.h"
#include "Serial_JMP.h"

/*
 * main.c
 */
void main(void) {
	WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer
	USB_setup(9600);
	MOTOR_ultra_setup();
	_BIS_SR(GIE);
	char command;

	int m1_speed = 0;
	int m2_speed = 0;
	int m3_speed = 0;
	int m4_speed = 0;
	int m5_speed = 0;
	int m6_speed = 0;

	while(1){
		USB_receive_byte(&command);
		/* For Up and Down */
		if(command == 'o'){
			if(m1_speed < MOTOR_CAP){
				m1_speed+=5;
				m2_speed+=5;
				m3_speed+=5;
				m4_speed+=5;
			}
		}else if(command == 'l'){
			if(m1_speed > -1*MOTOR_CAP){
				m1_speed-=5;
				m2_speed-=5;
				m3_speed-=5;
				m4_speed-=5;
			}
		}
		/* For front and back */
		else if(command == 'w'){
			if(m5_speed != m6_speed){
				m5_speed = 0;
				m6_speed = 0;
			}if(m5_speed < MOTOR_CAP){
				m5_speed += 5;
				m6_speed += 5;
			}
		}else if(command == 's'){
			if(m5_speed != m6_speed){
				m5_speed = 0;
				m6_speed = 0;
			}if(m5_speed > -1*MOTOR_CAP){
				m5_speed -= 5;
				m6_speed += 5;
			}
		}else if(command == 'a'){
			if(m5_speed == m6_speed){
				m5_speed = 0;
				m6_speed = 0;
			}if(m5_speed < MOTOR_CAP){
				m5_speed += 5;
				m6_speed -= 5;
			}
		}else if(command == 'd'){
			if(m5_speed == m6_speed){
				m5_speed = 0;
				m6_speed = 0;
			}if(m6_speed < MOTOR_CAP){
				m5_speed -= 5;
				m6_speed += 5;
			}
		}else if(command == 'x'){
			MOTOR_speed(0, 5);
			MOTOR_speed(0,8);
			m1_speed = 0;
			m2_speed = 0;
			m3_speed = 0;
			m4_speed = 0;
			m5_speed = 0;
			m6_speed = 0;
		}
		MOTOR_speed(m1_speed, 7);
		MOTOR_speed(m5_speed, 5);
		MOTOR_speed(m6_speed, 6);
		command = ' ';
	}
}
