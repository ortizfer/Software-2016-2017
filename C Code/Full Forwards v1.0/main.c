#include <msp430.h> 
#include "Serial_JMPv2.0.h"
#include "Motors_JMP.h"
#include "General_JMP.h"
#include "RAZOR_AHRS.h"

/*
 * main.c
 */

#define YAW_THRESHOLD 10


unsigned char tiemDone = 0;	 //Forward time done
int m1_speed = 0;
int m2_speed = 0;
int v_speed = 0;


void forward(unsigned int time, int speed){
	m1_speed = speed;
	m2_speed = speed;
	MOTOR_speed(speed, H_MOTORS);	//Sends speed to front two motors
	timeExceed(time, &tiemDone);
}

void allign(char direction){
	if((m1_speed + sign(direction)) <= MOTOR_CAP){
		m1_speed += sign(direction);
	}
	if((m2_speed - sign(direction)) <= MOTOR_CAP){
		m2_speed -= sign(direction);
	}
	MOTOR_speed(m1_speed, MOTOR5);
	MOTOR_speed(m2_speed, MOTOR6);
	__delay_cycles(200);
}



int main(void) {
    WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer
	USB_setup(9600);		// Set up USB connection
	MOTOR_ultra_setup();	// Set up all motors
	m1_speed = 0;			// Speed for one horizontal motor
	m2_speed = 0;			// Speed for second horizontal motor
	v_speed = 0;			// Speed for vertical motors


//	RAZOR_sngl_setup();		//Setup IMU
//	RAZOR_out_angles();		//Get angles from the IMU in binary format
//	RAZOR_refresh_value();	//Get one frame from the IMU
//
//
//	float offset = yaw;			//Off set for the measurements
//	float setPoint = 0.0;		//Operational set point
//	float difference = 0.0;


	char command = 0;				// Command to execute
	char arguments = 0;				// Arguments for commands
	char forwardsController = 0;	// Defines whether the controller in active
	unsigned int tiem = 0;			// Time variable
	int seped = 0; 		 			// Speed variable

	USB_getchar(&command, 'a');
	_BIS_SR(GIE);

	while(1){
		//Serial command processing
		if(command != 0){

			if(command == 'f'){ //Full forward?
				USB_println("Enter time from 0-9, x to exit");
				USB_getchar_b(&arguments);
				if(arguments > '0' && arguments < '9'){
					tiem = arguments - '0' + 1;
					USB_println("Enter speed from 0-9, x to exit");
					USB_getchar_b(&arguments);
					if(arguments > '0' && arguments < '9'){
						USB_println("Testing the Controller by moving");
						seped = MOTOR_CAP/10*(arguments - '0');
						forwardsController = 1;
//						RAZOR_refresh_value();
//						setPoint = yaw - offset;
						forward(tiem, seped);
					}else{
						USB_println("Invalid command");
					}
				}else{
					USB_println("Invalid command");
				}
//			}else if(command == 'c'){
//				USB_println("Testing the Controller staying still");
//				MOTOR_speed(0, V_MOTORS);
//				forwardsController = 1;
//				RAZOR_refresh_value();
//				setPoint = yaw - offset;
			}
			else if(command == 'w'){
				if(m1_speed != m2_speed){
					m1_speed = 0;
					m2_speed = 0;
				}if(m1_speed < MOTOR_CAP){
					m1_speed += 5;
					m2_speed += 5;
				}
				MOTOR_speed(m1_speed, 5);
				MOTOR_speed(m2_speed, 6);
			}else if(command == 's'){
				if(m1_speed != m2_speed){
					m1_speed = 0;
					m2_speed = 0;
				}if(m1_speed > -1*MOTOR_CAP){
					m1_speed -= 5;
					m2_speed -= 5;
				}
				MOTOR_speed(m1_speed, 5);
				MOTOR_speed(m2_speed, 6);
			}else if(command == 'a'){
				if(m1_speed == m2_speed){
					m1_speed = 0;
					m2_speed = 0;
				}if(m1_speed < MOTOR_CAP){
					m1_speed += 5;
					m2_speed -= 5;
				}
				MOTOR_speed(m1_speed, 5);
				MOTOR_speed(m2_speed, 6);
			}else if(command == 'd'){
				if(m1_speed == m2_speed){
					m1_speed = 0;
					m2_speed = 0;
				}if(m2_speed < MOTOR_CAP){
					m1_speed -= 5;
					m2_speed += 5;
				}
				MOTOR_speed(m1_speed, 5);
				MOTOR_speed(m2_speed, 6);
			}else if(command == 'o'){
				MOTOR_speed(++v_speed, V_MOTORS);
			}else if(command == 'l'){
				MOTOR_speed(--v_speed, V_MOTORS);
			}
			if(command == 'x'){
				forwardsController = 0;
				MOTOR_speed(0, V_MOTORS);
				MOTOR_speed(0, H_MOTORS);
			}
			command = 0;		//Commands processed - clear command queue
		//Enter other commands
		}

		//Enter align control
		if(forwardsController){												// Controller configuration
			if(tiemDone){													// If timeout is over
				MOTOR_speed(0, H_MOTORS);									// Turn off motors
				forwardsController = 0;										//
				tiemDone = 0;
				USB_println("Exited controller");
			}
			USB_println("Working on controller");
//			RAZOR_refresh_value();
//			//TODO - Handle discontinuity
//			difference = abs(yaw-offset) - abs(setPoint);
//			if(abs(difference) > YAW_THRESHOLD){
//				stopDelay();
//				allign(difference);
//				startDelay();
//			}
			__delay_cycles(500);
		}
		else{
			USB_println("Waiting for command");
			__delay_cycles(200000);
		}
	}
}
