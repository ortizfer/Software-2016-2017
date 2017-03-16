#include <msp430f5529.h>
#include "Motors_JMP.h"
/*
 * Pwm_JMP.c
 *
 *  Created on: Oct 26, 2016
 *      Author: Jose A. Montes Perez
 * Last Modification: Dec 21, 2016
 *
 * 	This file is utilized as a generic PWM generator
 * applied to ESC operations on the msp430f5529lp. 
 *	This supports up to four motor controller/servos 
 * at once. 
 * 
 * Wiring diagram:
 * Motor 1 -> P2.5
 * Motor 2 -> P2.4
 * Motor 3 -> P1.4
 * Motor 4 -> P1.3
 * 
 */

 
#define REFRESH_RATE 655
#define DEADBAND 75
#define RANGE 20

/***********************************************************************************
 *Function Description
 *		This function sets up all the motor specified in the wiring diagram to output ESC
 * compatible PWM signals. By default the will outup nothing (ground).
 *
 ***********************************************************************************/


void MOTOR_full_setup(){
	
	P2DIR |= BIT4 + BIT5;								// Setup motor 1 & 2 pins as output for pwm
	P2SEL |= BIT4 + BIT5;								// Select timer module over gpio
	
	P1DIR |= BIT4 + BIT3;								// Setup motor 3 & 4 pins as output for pwm
	P1SEL |= BIT4 + BIT3;								// Select timer module over gpio


	TA0CCR0 = REFRESH_RATE;						// Set the refresh rate of the pwm signal to 50Hz
	TA2CCR0 = REFRESH_RATE;						// Set the refresh rate of the pwm signal to 50Hz
	
	TA2CCTL1 = OUTMOD_7;            	             // Set Capture Compare Rregister 3 to reset/set mode
	TA2CCR1 = REFRESH_RATE;                       // No ouptut signal
	TA2CCTL2 = OUTMOD_7;            	             // Set Capture Compare Rregister 3 to reset/set mode
	TA2CCR2 = REFRESH_RATE;                       // No ouptut signal
	TA0CCTL2 = OUTMOD_7;                            // Set Capture Compare Rregister 3 to reset/set mode
	TA0CCR2 = 0REFRESH_RATE                      // No ouptut signal
	TA0CCTL3 = OUTMOD_7;		     				// Set Capture Compare Rregister 2 to reset/set mode
	TA0CCR3 = REFRESH_RATE;						// No output signal

	TA0CTL = TASSEL_1 + MC_1 + TACLR;       // ACLK, up mode, clear T
	TA2CTL = TASSEL_1 + MC_1 + TACLR;       // ACLK, up mode, clear T

}

/***********************************************************************************
 *Function Description
 *		This function sets up half the motor specified in the wiring diagram to output ESC
 * compatible PWM signals. The pins configured are for motor 1 & 2. By default the will outup nothing (ground).
 *
 ***********************************************************************************/

void MOTOR_half_setup(){
	
	P2DIR |= BIT4 + BIT5;								// Setup motor 1 & 2 pins as output for pwm
	P2SEL |= BIT4 + BIT5;								// Select timer module over gpio
	
	TA2CCR0 = REFRESH_RATE;						// Set the refresh rate of the pwm signal to 50Hz
	
	TA2CCTL1 = OUTMOD_7;            	             // Set Capture Compare Rregister 3 to reset/set mode
	TA2CCR1 = REFRESH_RATE;                       // No ouptut signal
	TA2CCTL2 = OUTMOD_7;            	             // Set Capture Compare Rregister 3 to reset/set mode
	TA2CCR2 = REFRESH_RATE;                       // No ouptut signal
	
	TA2CTL = TASSEL_1 + MC_1 + TACLR;       // ACLK, up mode, clear T
}



/***********************************************************************************
 *Function Description
 * 	This function controls the velocity that the motors turn in. It has two parameters, one for speed.
 *  and one for motor selection. The speed ranges from -100 to 100. To select a motor simply put the 
 *  desirted motors number from the wiring diagram in the motor varible. If you want to change all 
 *  the motors place 5 as the input.
 *
 ***********************************************************************************/

void MOTOR_speed(int speed, unsigned int motor){
	if((speed < 100) && (speed > -100 ) && (motor < 6)){			// Verify correct parameters
		int dutyCycle = speed*RANGE + DEADBAND;						// Calculate appropriate duty cycle
		int operations = (dutyCycle*ServoMS)/100;							// Calculate the appropriate register value
		TA0R = 0;																			// Reset timer count
		TA2R = 0;																			// Reset timer count
		switch (motor){																// Verify which motor to modify
			case 1: TA2CCR2=operations;break;								// Change speed of motor 1
			case 2: TA2CCR1=operations;break;								// Change speed of motor 2
			case 3: TA0CCR3=operations;break;								// Change speed of motor 3
			case 4: TA0CCR2=operations;break;								// Change speed of motor 4
			case 5: 																		// Change speed of all motors
				TA2CCR1 = operations;
				TA2CCR2 = operations;
				TA0CCR2 = operations;
				TA0CCR3 = operations;
				break;
			default: break;															// Do nothing
		}
	}
}
