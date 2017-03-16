#include <msp430.h> 
#include "Motors_JMP.h"
#include "Serial_JMP.h"
#include "General_JMP.h"
#include "typecast.h"


/*
 * main.c
 */
int main(void) {
	WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer
	USB_setup(9600);
	_BIS_SR(GIE);
	MOTOR_ultra_setup();

	char command;
	char vert = 0;
	int m1_speed = 0;
	int m2_speed = 0;
	int m3_speed = 0;
	int m4_speed = 0;
	int m5_speed = 0;
	int m6_speed = 0;

	while(1){

		USB_receive_byte(&command);
		/* For Up and Down */
		if(command != 0x00){
			if(command == 't'){
				if(vert){
					vert = 0;
				}else{
					vert = 1;
				}
			}
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
					m6_speed -= 5;
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
				MOTOR_speed(0,7);
				MOTOR_speed(0,8);
				m1_speed = 0;
				m2_speed = 0;
				m3_speed = 0;
				m4_speed = 0;
				m5_speed = 0;
				m6_speed = 0;
			}else if(command == '1'){
				if(!vert){
					m1_speed = MOTOR_CAP*10/100;
					m2_speed = MOTOR_CAP*10/100;
					m3_speed = MOTOR_CAP*10/100;
					m4_speed = MOTOR_CAP*10/100;
				}else{
					m5_speed = MOTOR_CAP*10/100;
					m6_speed = MOTOR_CAP*10/100;
				}
			}else if(command == '2'){
				if(!vert){
					m1_speed = MOTOR_CAP*20/100;
					m2_speed = MOTOR_CAP*20/100;
					m3_speed = MOTOR_CAP*20/100;
					m4_speed = MOTOR_CAP*20/100;
				}else{
					m5_speed = MOTOR_CAP*20/100;
					m6_speed = MOTOR_CAP*20/100;
				}
			}else if(command == '3'){
				if(!vert){
					m1_speed = MOTOR_CAP*30/100;
					m2_speed = MOTOR_CAP*30/100;
					m3_speed = MOTOR_CAP*30/100;
					m4_speed = MOTOR_CAP*30/100;
				}else{
					m5_speed = MOTOR_CAP*30/100;
					m6_speed = MOTOR_CAP*30/100;
				}
			}else if(command == '4'){
				if(!vert){
					m1_speed = MOTOR_CAP*40/100;
					m2_speed = MOTOR_CAP*40/100;
					m3_speed = MOTOR_CAP*40/100;
					m4_speed = MOTOR_CAP*40/100;
				}else{
					m5_speed = MOTOR_CAP*40/100;
					m6_speed = MOTOR_CAP*40/100;
				}
			}else if(command == '5'){
				if(!vert){
					m1_speed = MOTOR_CAP*50/100;
					m2_speed = MOTOR_CAP*50/100;
					m3_speed = MOTOR_CAP*50/500;
					m4_speed = MOTOR_CAP*50/100;
				}else{
					m5_speed = MOTOR_CAP*50/100;
					m6_speed = MOTOR_CAP*50/100;
				}
			}else if(command == '6'){
				if(!vert){
					m1_speed = MOTOR_CAP*60/100;
					m2_speed = MOTOR_CAP*60/100;
					m3_speed = MOTOR_CAP*60/100;
					m4_speed = MOTOR_CAP*60/100;
				}else{
					m5_speed = MOTOR_CAP*60/100;
					m6_speed = MOTOR_CAP*60/100;
				}
			}else if(command == '7'){
				if(!vert){
					m1_speed = MOTOR_CAP*70/100;
					m2_speed = MOTOR_CAP*70/100;
					m3_speed = MOTOR_CAP*70/100;
					m4_speed = MOTOR_CAP*70/100;
				}else{
					m5_speed = MOTOR_CAP*70/100;
					m6_speed = MOTOR_CAP*70/100;
				}
			}else if(command == '8'){
				if(!vert){
					m1_speed = MOTOR_CAP*80/100;
					m2_speed = MOTOR_CAP*80/100;
					m3_speed = MOTOR_CAP*80/100;
					m4_speed = MOTOR_CAP*80/100;
				}else{
					m5_speed = MOTOR_CAP*80/100;
					m6_speed = MOTOR_CAP*80/100;
				}
			}else if(command == '9'){
				if(!vert){
					m1_speed = MOTOR_CAP*90/100;
					m2_speed = MOTOR_CAP*90/100;
					m3_speed = MOTOR_CAP*90/100;
					m4_speed = MOTOR_CAP*90/100;
				}else{
					m5_speed = MOTOR_CAP*90/100;
					m6_speed = MOTOR_CAP*90/100;
				}
			}else if(command == '0'){
				if(!vert){
					m1_speed = MOTOR_CAP;
					m2_speed = MOTOR_CAP;
					m3_speed = MOTOR_CAP;
					m4_speed = MOTOR_CAP;
				}else{
					m5_speed = MOTOR_CAP;
					m6_speed = MOTOR_CAP;

				}
			}else if(command == 'b'){
				m5_speed = MOTOR_CAP;
				m6_speed = -1*MOTOR_CAP;
			}else if(command == 'n'){
				m5_speed = -1*MOTOR_CAP;
				m6_speed = MOTOR_CAP;
			}
			MOTOR_speed(m1_speed, 1);
			MOTOR_speed(m2_speed, 2);
			MOTOR_speed(m3_speed, 3);
			MOTOR_speed(m4_speed, 4);

			MOTOR_speed(m5_speed, 5);
			MOTOR_speed(m6_speed, 6);
			command = 0;
		}
	}
}
