
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
