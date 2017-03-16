#include <msp430.h>
#include "General_JMP.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
 * General_JMP.c
 *
 *  Created on: Oct 26, 2016
 *      Author: jose.montes1
 *
 * A collection of of methods utilized in
 * the laboratories for MICRO 2
 *
 *
 */





///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////// Timer Commands ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/*\****************************************************************
 *Function Description
 *		Disables interrupts that you dont want to interrupt a delay
 *Parameters
 *		On - set 1 to enable interrupts and set a 0 to disable the
 *			interrupts
 *
 *\****************************************************************/

void interrupts(char on){
	if(on){

	}
	else{
	}
}

/*\****************************************************************
 *Function Description
 *		Delays the micro a certain amount of time while setting
 *		it in low power mode.
 *Parameters
 *		Miliseconds - miliseconds to wait
 *
 *\****************************************************************/

void delay(unsigned long miliSeconds){
	unsigned long operations = (32768*miliSeconds)/1000;
	TB0CTL |= TBCLR; 				// Clear Timer content
	TB0CCR0 = operations;			// Set the timer period
	TB0CTL |= TBSSEL_1;				// Use aclk
	TB0CTL |= MC_1;					// Use up mode

	interrupts(0);					// Disable interrupts
	TB0CCTL0 |= CCIE;				// Enable Interrupt
	__bis_SR_register(GIE + LPM0_bits);	// halt cpu
	interrupts(1);					// Enable interrupts


	return;
}
/*\****************************************************************
 *Function Description
 *		Timer B interrupt. Disables the running timer delay
 *Parameters
 *
 *
 *\****************************************************************/

#pragma vector = TIMER0_B0_VECTOR
__interrupt void TIMER_B0(void){

	TB0CTL &= ~MC_1;				//Stop timer
	TB0CTL |= MC_0;					//Make sure its stopped
	LPM0_EXIT;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////// Lcd Commands
/*\****************************************************************
 *Function Description
 *		Sends a command to the lcd
 *Parameters
 *		cmd - Command to sent the LCD
 *
 *\****************************************************************/
void nibble() {

	E_high;
	delay(1);
	E_low;

}

void command(char cmd) {

	char c = cmd;					// Locally store command
	P2OUT &= ~0xF0; 				// CLEAR MSBs
	P2OUT |= (c & 0xF0); 			// data into port
	RS_low; 						// CLEAR RS bit, sending command
	nibble(); 						// Send the nibble
	c = c << 4; 					// Shift data 4 bits
	P2OUT &= ~0xF0; 				// CLEAR MSBs
	P2OUT |= (c & 0xF0); 			// Shifted data into port
	nibble(); 						// Send shifted nibble
	P2OUT &= ~0xF0; 				// CLEAR MSBs

}
/*\****************************************************************
 *Function Description
 *		Writes data in the form of a char onto the LCD
 *Parameters
 *		data - Char to send
 *
 *\****************************************************************/

void write(char data) {

	char d = data;
	P2OUT &= ~0xF0; 				//CLEAR MSBs
	P2OUT |= (d & 0xF0); 					// data into port
	RS_high; 						//ENABLE RS bit, sending write
	nibble(); 						//send the nibble
	d = d << 4; 					// shift data 4 bits
	P2OUT &= ~0xF0; 				//CLEAR MSBs
	P2OUT |= (d & 0xF0); 			//shifted data into port
	nibble(); 						//send shifted nibble
	P2OUT &= ~0xF0; 				//CLEAR MSBs

}
/*\****************************************************************
 *Function Description
 *		Writes a char* onto the LCD
 *Parameters
 *		str - String to write
 *
 *\****************************************************************/

void write_str(char *str) {
	while(*str) {
		write(*str);
		str++;
	}
}

/**
 * cursor to top line of LCD
 */
void cursor_top() {
	command(0x00);
	delay(10);
}

/**
 * cursor to bottom line of LCD
 */
void cursor_bot() {
	command(0xC0);
}

/**
 * clears the screen of LCD
 */
void clear_lcd() {
	command(0x01);
	delay(10);
	cursor_top();
}
/*\****************************************************************
 *Function Description
 *		Initialices the LCD display
 *Parameters
 *
 *
 *\****************************************************************/

void lcdInit() {

	P2DIR |= 0xFF; 				// P2 as OUTPUT
	P2OUT &= ~0xFF; 			//CLEAR
	P2OUT |= 0x30; 				// Wake-up command
	delay(100);
	nibble(); 					// wake up 1
	delay(10);
	nibble(); 					// wake up 2
	delay(10);
	nibble(); 					// wake up 3
	delay(10);
	P2OUT &= ~0x30;
	P2OUT |= 0x20; 				// set 4 bit interface
	nibble();
	command(0x28);				// 4 bit / 2-line
	delay(10);
	command(0x10); 				// set cursor
	delay(10);
	command(0x0F); 				// display ON: blinking cursor
	delay(10);
	command(0x01);				// clear display
	delay(10);
	command(0x02);				// set cursor to home
	delay(10);
	command(0x06);				// entry mode set
	delay(10);

}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////// Number methods

/*\****************************************************************
 *Function Description
 *		Reverse the char array you input
 *Parameters
 *
 *
 *\****************************************************************/


void reverse(char s[]){
    int i, j;
    char c;

    for (i = 0, j = strlen(s)-1; i<j; i++, j--) {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}

/*\****************************************************************
 *Function Description
 *		Converts an integet into a char array
 *Parameters
 *		n - number to convert
 *		s - array to fill
 *
 *\****************************************************************/


void itoa(int n, char s[]){

	 int i, sign;

     if ((sign = n) < 0)  /* record sign */
         n = -n;          /* make n positive */
     i = 0;
     do {       /* generate digits in reverse order */
         s[i++] = n % 10 + '0';   /* get next digit */
     } while ((n /= 10) > 0);     /* delete it */
     if (sign < 0)
         s[i++] = '-';
     s[i] = '\0';
     reverse(s);
 }

