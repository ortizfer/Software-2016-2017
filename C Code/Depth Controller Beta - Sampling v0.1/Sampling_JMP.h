/*
 * Sampling_JMP.h
 *
 *  Created on: Mar 2, 2017
 *      Author: Jose A. Montes
 *
 *      Contains a series of commands directed towards
 * sampling in a controlled fashion.
 *
 * ABSTRACT DECLARATIONS
 * -Note that the user must implement their own sample funtcion
 * as the SAMPLE_measure() method.
 *
 * HARDWARE DEPENDENCIES
 * -This library utilizes the TIMERA1 register
 */

#ifndef SAMPLING_JMP_H_
#define SAMPLING_JMP_H_

void BT_timeout_setup(int miliseconds);
void BT_restart_timeout();
void BT_stop_timeout();

volatile char _sample;

void SAMPLE_measure();
void SAMPLE_enable_interrupt();
__interrupt void TIMER1_A0_ISR(void);




#endif /* SAMPLING_JMP_H_ */
