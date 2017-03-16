/*
 * Razer_AHRS.c
 *
 * 	This code works to communicate the Sparkfun Razor AHRS[1] to the MSP430F5529 micro-controller[2].
 * 	Contains the implementation to the API defined in the Razer_AHRS.h header.
 *  Code is based on the firnmware found at [3]
 *
 * Depends on Serial_JMP.h
 *
 * Wiring diagram:
 * P3.3 -> TX@Razor
 * P3.4 -> RX@Razor
 *
 * USB -> PC COM PORT
 *
 *
 *  Created on: Feb 11, 2017
 *      Author: Jose A. Montes Perez
 *
 *  References:
 *  [1] https://www.sparkfun.com/products/retired/10736 - Sparkfun Razor IMU
 *  [2] http://www.ti.com/product/MSP430F5529 - MSP430F5529
 *  [3] https://github.com/Razor-AHRS/razor-9dof-ahrs
 *
 */

#include <msp430.h>
#include <stdlib.h>
#include "Razer_AHRS.h"
#include "Serial_JMP.h"


char angle_output;


void RAZER_setup(){
	UART_setup(IMU_BAUD_RATE);
}

void RAZER_out_angles(){
	UART_print("#o0");
	UART_print("#ob");
	angle_output = 1;
}

void RAZER_out_sensors(){
	UART_print("#o0");
	UART_print("#oscb");
	angle_output = 0;
}

void RAZER_read_values(){
	int i;
	char *inBuffer;
	inBuffer = (char *) malloc(IMU_BUFFER);

	UART_print("#f");

	if(angle_output){
		for(i = 12; i > 0; i--){
			UART_receive_byte(inBuffer + i);
		}
		yaw = *(float *)(inBuffer);
		pitch = *(float *)(inBuffer + 4);
		roll = *(float *)(inBuffer + 8);
	}else{
		for(i = 36; i > 0; i--){
			UART_receive_byte(inBuffer +i);
		}
		acc_x = *(float *) (inBuffer);
		acc_y = *(float *) (inBuffer + 4);
		acc_z = *(float *) (inBuffer + 8);

		mag_x = *(float *) (inBuffer + 12);
		mag_y = *(float *) (inBuffer + 16);
		mag_z = *(float *) (inBuffer + 20);

		gyr_x = *(float *) (inBuffer + 24);
		gyr_y = *(float *) (inBuffer + 28);
		gyr_z = *(float *) (inBuffer + 32);
	}
	free(inBuffer);
}




/****************************************************************************************************
 *Function Description
 * 	This Function allows you to manually control the output rate of the IMU in non-continuous mode.
 * The parameter milliseconds defines the refresh rate and has a minimum of 20ms and a maximum of
 * 10000ms.
 *
 *
 *
 *****************************************************************************************************/
void TIMER_setup(int milliseconds){
	if(milliseconds > 20 && milliseconds < 1000){
		int operations = ((long) milliseconds << 16)/1000;	// Conversion from milliseconds to discrete operations
		TA0CCR0 = operations;								// Set frequency in CCR0 register
		TA0CTL = TASSEL_2 + MC_1 + TACLR;					// Set clock to ACLK, Up mode, Clear counter
		TA0CCTL0 = CCIE;									// Enable interrupts
	}
}
// Complimentary ISR to timer. This sends the request for the data to the IMU
#pragma vector=TIMER0_A0_VECTOR
__interrupt void TIMER0_A0_ISR(void){
	__bic_SR_register_on_exit(LPM0_bits);
}




