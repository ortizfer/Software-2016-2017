/*
 * Pwm_JMP.h
 *
 *  Created on: Oct 26, 2016
 *      Author: jose.montes1
 */

#ifndef MOTORS_JMP_H_
#define MOTORS_JMP_H_

#define ServoMS 655
#define DEADBAND 1500
#define RANGE 500
#define ESCRANGE 400


void MOTOR_full_setup();
void MOTOR_half_setup();
void MOTOR_speed(int speed, unsigned int motor);


#endif /* MOTORS_JMP_H_ */
