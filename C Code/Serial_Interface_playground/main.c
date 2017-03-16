#include <msp430.h> 
#include "Serial_JMP.h"
#include <stdlib.h>
/*
 * main.c
 */

//UART Interrupt Vector

void main(void) {
    WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer

    USB_setup(9600);
	_BIS_SR(GIE);
	char cahr;
	char *command;
	command = (char *) malloc(50);
	USB_getchar(&cahr, 'a');
	while(1){
		USB_print("Received: ");
		USB_putchar(cahr);
		USB_println(" ");
		if(cahr == 'g'){
			USB_print("Testing stop: ");
			USB_getline_b(command);
			USB_print(command);
			cahr = 0;
		}
		__delay_cycles(50000);
	}
}
