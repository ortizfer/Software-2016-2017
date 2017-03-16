/*
 * Razer_AHRS.h
 *
 *  Created on: Feb 11, 2017
 *      Author: RathK
 */

#ifndef RAZER_AHRS_H_
#define RAZER_AHRS_H_


#define IMU_BAUD_RATE 9600		//Baud Rate for communicating with the sensor
#define IMU_SAMPLE_RATE 60		//Suggested sample rate in milliseconds
#define IMU_BUFFER 60			//Malloc buffer size with slight overshoot



//Variables that store the values for a particular
//angle
float yaw,pitch,roll;
//Variables were the values for the particular
//sensor are sotred
float acc_x,acc_y,acc_z;
float mag_x,mag_y,mag_z;
float gyr_x,gyr_y,gyr_z;

void RAZER_setup();
void RAZER_out_angles();
void RAZER_out_sensors();
void RAZER_read_values();

void TIMER_setup(int milliseconds);
__interrupt void TIMER0_A0_ISR(void)


#endif /* RAZER_AHRS_H_ */
