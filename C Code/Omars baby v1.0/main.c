
/***********************************************************************************
 *This is the first attempt to implement a depth controller for proteus
 *Author: Omar Gonzalez
 *Date: march 2, 2017
 *
 ***********************************************************************************/




#include <msp430.h> 
#include "Motors_JMP.h"
#include "Serial_JMP.h"
#include "General_JMP.h"
#include "typecast.h"
#include "MS5837-30BA.h"

#define MSDELAY 50

int32 pressure;
int32 temp;
int samp;

#define Controller_Gain 23.0

void SAMPLE_measure(){
	PRESSURE_start_conversion();
	pressure = PRESSURE_get_pressure();
	temp = PRESSURE_get_temperature();

}



/*
 * main.c
 */
int main(void) {
	WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer
	I2C_setup(400000);			//Start I2C communication at 100k bps
	USB_setup(9600);
	USB_println("Initializing setup");
	_BIS_SR(GIE);
	MOTOR_full_setup();
	PRESSURE_calibrate();
	USBBuff = 0;
	temp = 0;

	int m1_speed = 0;
	int m2_speed = 0;
	int m3_speed = 0;
	int m4_speed = 0;
	char controller_initialized = 0;
	float reference = 0;
	float actual_depth_bars = 0;
	float actual_depth_milibars = 0;
	float actual_depth_feet = 0;
	float error = 0;
	float output = 0;


	float actual_depth_pwm;
	//int Controller_Gain;
	int USB_Buffer = 0;

	USB_receive_non_blocking();
	USB_print("System initialized");


	while(1){
		if(USBBuff != 0){
			USB_print("Received command: ");
			USB_transmit_byte(USBBuff);
			USB_println(".");
			if(USBBuff >= '0' && USBBuff <= '9'){
				USB_Buffer = USBBuff - '0';      // converts to decimal value of each number pressed
			}else if(USBBuff == 'q'){
				USB_Buffer = 10;
			}else if(USBBuff == 'w'){
				USB_Buffer = 11;
			}else if(USBBuff == 'e'){
				USB_Buffer = 12;
			}else if(USBBuff == 'r'){
				USB_Buffer = 13;
			}else if(USBBuff == 't'){
				USB_Buffer = 14;
			}else if(USBBuff == 'y'){
				USB_Buffer = 15;
			}else if(USBBuff == 'u'){
				USB_Buffer = 16;
			}else if(USBBuff == 'x'){
				controller_initialized = 0;
				USB_Buffer = 17;
			}else if(USBBuff == 'h'){
				controller_initialized = 1;
			}
			USBBuff = 0;
		}
		if(controller_initialized){
			USB_println("Controller looping");
			SAMPLE_measure();
			USB_println("Read pressure");
			reference = (USB_Buffer*6.25);                        //aquire data from command listening to PC
			actual_depth_bars = (((float) pressure)/10000);       // convert bars to milibars
			actual_depth_milibars = (actual_depth_bars*33.4552565551477); //convert milibars to feet
			actual_depth_feet = (actual_depth_milibars - 29);  // calibrate depending on altitude above sea
			actual_depth_pwm = (actual_depth_feet*6.25);



			// equation of differences for proportional controller

			error = (reference - actual_depth_pwm);      //calculate error

			// Proportional Controller

			//Controller_Gain = 23.0;

			output = Controller_Gain*error;

			// send controller output to motors
			if(USB_Buffer == 17)
				output = 0;

			m1_speed = output;
			m2_speed = output;
			m3_speed = output;
			m4_speed = output;


			/* Satutration*/

			if((m1_speed) > MOTOR_CAP)
				m1_speed = MOTOR_CAP;
			if((m2_speed) > MOTOR_CAP)
				m2_speed = MOTOR_CAP;
			if(m3_speed > MOTOR_CAP)
				m3_speed = MOTOR_CAP;
			if(m4_speed > MOTOR_CAP)
				m4_speed = MOTOR_CAP;
			if((m1_speed) < -1*MOTOR_CAP)
				m1_speed = -1*MOTOR_CAP;
			if((m2_speed) < -1*MOTOR_CAP)
				m2_speed = -1*MOTOR_CAP;
			if(m3_speed < -1*MOTOR_CAP)
				m3_speed = -1*MOTOR_CAP;
			if(m4_speed < -1*MOTOR_CAP)
				m4_speed = -1*MOTOR_CAP;

			MOTOR_speed(m1_speed, 1);
			MOTOR_speed(m2_speed, 2);
			MOTOR_speed(m3_speed, 3);
			MOTOR_speed(m4_speed, 4);
		}
		else{
			USB_println("Not doing anything");
			MOTOR_speed(0,5);
			__delay_cycle(20000);
		}
		//--------------------------------------------------------------------------------------------------------------------
	}
}


