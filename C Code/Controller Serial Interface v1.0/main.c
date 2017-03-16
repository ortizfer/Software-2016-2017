#include <msp430.h> 
#include "Serial_JMPv2.0.h"
#include "typecast.h"
/*
 * main.c
 * General skeleton for controller implementation
 * Jose Montes
 *
 *
 */


//Struct utilized to keep tract of the conditions of the controller
struct serialConditions {
	uint8 depthControllerEnabled : 1;		//Determines whether the depth controller is enabled
	uint8 alignControllerEnabled : 1;		//Determines whether the align controller is enabled
	uint8 forwardsDeadreckoning : 2;		//Determines if you go forwards by time or not

	uint8 systemRunning : 1;				//Determines whether the system starts or not
	// 0 - not running | 1 - running

	uint8 terminalIO : 1;					//Determines if the system receives input from the script or from the user
	/* 0 - input from script | 1 - input from terminal */


	uint8 firstCommand : 1;					//Determines if it is the first input
	uint8 secondCommand : 1;				//Determines if it is the second command
	uint8 thirdCommand : 1;					//Determines if it is the third command

	uint8 clearInput : 1; 					//Determines when to clear inputs (complete or invalid command)
	uint8 validCommand : 1;					//Determines whether it is a valid command or not

	//	uint8 printFeedbackFrame : 1;			//Determines when to print an output frame from the status
	//	uint8 printContinousFrames : 1;			// TODO - maybe
	//	uint8 printStatusFrame : 1;				//Determines when to print a system status frame
};



//Use this to output information about the current stage
void printInputFeedback(int operatorNumber, char command){
	switch(operatorNumber){
	case 1: USB_print("Entered first operator: "); break;
	case 2: USB_print("Entered second operator: "); break;
	case 3: USB_print("Entered third operator: "); break;
	default: break;
	}
	USB_putchar(command);
	USB_println(" ");
}


#define invalidCommand() conditions.validCommand = 0; conditions.clearInput = 1





int main(void) {
	WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer
	USB_setup(9600);
	_BIS_SR(GIE);

	struct serialConditions conditions = {0,0,0,0,1,0,0,0,0,1};

	/* Controller shit */


	int8 commands[4];	//Command buffer
	commands[0] = 0;	//First operator
	commands[1] = 0;	//Second operator
	commands[2] = 0;	//Third operator
	commands[3] = 0;	//Trash collector


	while(!conditions.systemRunning){ 							//Verify that the system is enabled
		USB_println("Press 's' to start the system");			//Print usage to user
		USB_getchar(&commands[0], 'b');								//Get input from user in blocking mode
		if(*commands == 's'){									//Error check input
			conditions.systemRunning = 1;
		}
	}
	USB_println("Awaiting command");
	commands[0] = 0;
	USB_getchar(&commands[0], 'a');
	conditions.clearInput = 1;
	while(1){

		/* Enter command management /
		 * o - depth controller - required more operands
		 * a* - alignment controller - requires more operands
		 * x - exit all
		 * f - go forwards a certain amount of time - required more operands
		 * b - go backwards a certain amount of time - required more operands
		 * wasd - horizontal control keys
		 * t - print user mode
		 * y - print script mode
		 *  (* - means not implemented)
		 */
		if(commands[0] != 0  && conditions.systemRunning){
			/* Print feedback frame and set operator to second command */
			if(conditions.firstCommand){				//Verify so you only print once (to avoid spam)
				printInputFeedback(1,commands[0]);		//Print feedback to the user
				USB_getchar(&commands[1], 'a');			//Set UART receive to next value
				conditions.firstCommand = 0;			//Disable so you don't enter this if anymore
			}
			/* Enter depth controller Commands */
			if(commands[0] == 'o'){

				/* Depth controller options
				 * 0-9 Give set point corresponding to feet
				 * q - Place the set point at 11 feet
				 * w - Place the set point at 12 feet
				 * e - Place the set point at 13 feet
				 * r - Place the set point at 14 feet
				 * t - Place the set point at 15 feet
				 * y - Place the set point at 12 feet
				 *
				 * g - set the gain of the controller - requires other operand
				 *
				 * x - exit vertical controller and resets vertical motors
				 *
				 */

				/* if command arrives */
				if(commands[1] != 0){
					/* Print feedback frame and set operator to second command */
					if(conditions.secondCommand){				//Verify so you only print once (to avoid spam)
						printInputFeedback(2,commands[1]);		//Print feedback to the user
						USB_getchar(&commands[2], 'a');			//Set UART receive to next value
						conditions.secondCommand = 0;			//Disable so you don't enter this if anymore
					}

					/* Set point and enable controller commands */
					if(commands[1] >= '0' && commands[1] <= '9'){
						//TODO - place set point and turn on controller
						conditions.clearInput = 1;
						conditions.depthControllerEnabled = 1;
					}else if(commands[1] == 'q'){
						//TODO - place set point and turn on controller
						conditions.clearInput = 1;
						conditions.depthControllerEnabled = 1;
					}else if(commands[1] == 'w'){
						//TODO - place set point and turn on controller
						conditions.clearInput = 1;
						conditions.depthControllerEnabled = 1;
					}else if(commands[1] == 'e'){
						//TODO - place set point and turn on controller
						conditions.clearInput = 1;
						conditions.depthControllerEnabled = 1;
					}else if(commands[1] == 'r'){
						//TODO - place set point and turn on controller
						conditions.clearInput = 1;
						conditions.depthControllerEnabled = 1;
					}else if(commands[1] == 't'){
						//TODO - place set point and turn on controller
						conditions.clearInput = 1;
						conditions.depthControllerEnabled = 1;
					}else if(commands[1] == 'y'){
						//TODO - place set point and turn on controller
						conditions.clearInput = 1;
						conditions.depthControllerEnabled = 1;
					}

					/* Turn of controller command */
					else if(commands[1] == 'x'){
						//TODO - turn off motors and turn off controller
						conditions.clearInput = 1;
						conditions.depthControllerEnabled = 0;
					}

					/* Set Gain command */
					else if(commands[1] == 'g'){
						/* Set gain command
						 * 0 - 9 Sets the gain of the controller to the input value
						 */
						if(commands[2] != 0){
							/* Print feedback to user */
							if(conditions.thirdCommand){				//Verify so you only print once (to avoid spam)
								printInputFeedback(3,commands[2]);		//Print feedback to the user
								USB_getchar(&commands[3], 'a');			//Set UART receive to next value
								conditions.thirdCommand = 0;			//Disable so you don't enter this if anymore
							}
							/*Verify proper command */
							if(commands[2] >= '0' && commands[2] <= '9'){
								//TODO - set the gain to the value at command
								conditions.clearInput = 1;
							}
							/* Invalid third Command */
							else{
								invalidCommand();
							}
						}
					}
					/*Invalid second command */
					else{
						invalidCommand();
					}
				}
			}


			/* Enter Align Controller Commands */
			//else if(commands[0] == 'a'){
			//TODO - Leave this until the controller is implemented
			//}


			/* Enter forwards by a certain amount */
			else if(commands[0] == 'f'){
				/* Forwards input
				 * 0-9 Receive the amount of time you want to wait
				 * 0 means 1 second, 9 means 10
				 */
				if(commands[1] != 0){
					/* Print feedback to user */
					if(conditions.secondCommand){				//Verify so you only print once (to avoid spam)
						printInputFeedback(2,commands[1]);		//Print feedback to the user
						USB_getchar(&commands[2], 'a');			//Set UART receive to next value
						conditions.secondCommand = 0;			//Disable so you don't enter this if anymore
					}

					/* Set the time variable and go on */
					if(commands[1] >= '0' && commands[1] <= '9'){
						//TODO - set the time variable
						conditions.forwardsDeadreckoning = 1;
						conditions.clearInput = 1;
					}
					/*Invalid second command */
					else{
						invalidCommand();
					}
				}
			}

			/* Enter backwards by a certain amount */
			else if(commands[0] == 'b'){
				/* Backwards input
				 * 0-9 Receive the amount of time you want to wait
				 * 0 means 1 second, 9 means 10
				 */
				if(commands[1] != 0){
					/* Print feedback to user */
					if(conditions.secondCommand){				//Verify so you only print once (to avoid spam)
						printInputFeedback(2,commands[1]);		//Print feedback to the user
						USB_getchar(&commands[2], 'a');			//Set UART receive to next value
						conditions.secondCommand = 0;			//Disable so you don't enter this if anymore
					}

					/* Set the time variable and go on */
					if(commands[1] >= '0' && commands[1] <= '9'){
						//TODO - set the time variable
						conditions.forwardsDeadreckoning = 2;
						conditions.clearInput = 1;
					}
					/*Invalid second command */
					else{
						invalidCommand();
					}
				}
			}


			/* Manual control operation - go forwards - if tilting stop*/
			else if(commands[0] == 'w'){
				/* TODO - if(m5_speed != m6_speed){
					m5_speed = 0;
					m6_speed = 0;
				}if(m5_speed < MOTOR_CAP){
					m5_speed += 5;
					m6_speed += 5;
				}*/

				/* Manual control operation */
			}else if(commands[0] == 's'){
				/*TODO	if(m5_speed != m6_speed){
					m5_speed = 0;
					m6_speed = 0;
				}if(m5_speed > -1*MOTOR_CAP){
					m5_speed -= 5;
					m6_speed -= 5;
				}*/
			}else if(commands[0] == 'a'){
				/* TODO	if(m5_speed == m6_speed){
					m5_speed = 0;
					m6_speed = 0;
				}if(m5_speed < MOTOR_CAP){
					m5_speed += 5;
					m6_speed -= 5;
				}*/
			}else if(commands[0] == 'd'){
				/*TODO if(m5_speed == m6_speed){
					m5_speed = 0;
					m6_speed = 0;
				}if(m6_speed < MOTOR_CAP){
					m5_speed -= 5;
					m6_speed += 5;
				}*/
			}

			/* Change the input setting to User mode */
			else if(commands[0] == 'u'){
				conditions.terminalIO = 1;
				conditions.clearInput = 1;
			}

			/*Changes the input settings to the Script mode */
			else if(commands[0] == 'y'){
				conditions.terminalIO = 0;
				conditions.clearInput = 1;

			}


			/* Halt everything */
			else if(commands[0] == 'x'){
				//TODO - turn off motors
				conditions.alignControllerEnabled = 0;
				conditions.depthControllerEnabled = 0;
				conditions.systemRunning = 0;
				conditions.clearInput = 1;
			}
			/*Invalid first operand */
			else{
				invalidCommand();
			}
		}if(commands[0] != 0 && !conditions.systemRunning){
			if(commands[0] == 's'){
				USB_println("Restarting the system");
				conditions.systemRunning = 1;
				conditions.clearInput = 1;
			}
		}

		/* Reset the input state if you have a valid or invalid command */
		if(conditions.clearInput){

			if(conditions.validCommand){
				USB_println("Entered a valid command");
			}else{
				USB_println("Entered a invalid command");
			}
			conditions.validCommand = 1;					//Asume a valid command

			commands[0] = 0;
			commands[1] = 0;
			commands[2] = 0;

			conditions.firstCommand = 1;
			conditions.secondCommand = 1;
			conditions.thirdCommand  = 1;

			USB_getchar(&commands[0], 'a');
			conditions.clearInput = 0;

		}

		if(conditions.systemRunning){

			/* Depth controller section*/
			if(conditions.depthControllerEnabled){
				USB_println("Depth controller working");
				__delay_cycles(20000);
			}

			/* Align Controller section*/
			if(conditions.depthControllerEnabled){
			}

			/* WASD control section*/
			if(!conditions.forwardsDeadreckoning){
			}

			/* Forwards and backwards section */
			if(conditions.forwardsDeadreckoning){
			}

			/* Print usage to user */
			if (conditions.terminalIO){
			}

			/* Prints usage to the script */
			if (!conditions.terminalIO){
			}

		}
	}
}
