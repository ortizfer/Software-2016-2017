/*
 * Pwm_JMP.h
 *
 *  Created on: Oct 26, 2016
 *      Author: jose.montes1
 */

#ifndef MOTORS_JMP_H_
#define MOTORS_JMP_H_

#define MOTOR_CAP 40
#define MOTOR1 1
#define MOTOR2 2
#define MOTOR3 3
#define MOTOR4 4
#define MOTOR5 5
#define MOTOR6 6
#define V_MOTORS 7
#define H_MOTORS 8



void MOTOR_ultra_setup();
void MOTOR_full_setup();
void MOTOR_half_setup();
void MOTOR_speed(int speed, unsigned int motor);


#endif /* MOTORS_JMP_H_ */
