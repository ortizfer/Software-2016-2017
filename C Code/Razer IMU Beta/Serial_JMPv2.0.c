#include <msp430F5529.h>
#include "Serial_JMPv2.0.h"
#include "General_JMP.h"
/*
 * Serial_JMP.c
 *
 *  Created on: Oct 25, 2016
 *	Last Modification: Dec 20, 2016
 *	Changelog comment: Modified I2C protocol
 *
 *  Author: Jose A. Montes Perez
 *
 *
 *  This file contains implementations
 *  of the I2C and UART protocols,
 *  including some misc functions for
 *  the msp430f5529 MCU
 */


////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////UART functionality
/*\**********************************************************************************************************
 * Function Description
 *    Sets up the baud generator for a specific frequency
 * Parameters-
 * 	baudRate - defines the baud rate for communication
 * 		valid frequencies are 9600 and its multiples up to
 * 		115200. Suggested low frequency
 *\**********************************************************************************************************/

char *UARTBuff;										//Modify serial code to use pointers instead of global variables - protip: use pointer to UARTBuf
char UARTBlock;
char wasUARTBlock;

void UART_setup(unsigned long baudRate){
	P3SEL = BIT3+BIT4;                        // P3.4,5 = USCI_A0 TXD/RXD
	P3REN = BIT3;							// Set up resistor for BT module
	P3OUT = BIT3;							// Make it pull up
	UCA0CTL1 |= UCSWRST;                      // **Put state machine in reset**
	UCA0CTL1 |= UCSSEL_2;                     // CLK = SUBMAINCLK
	switch(baudRate){
	case 9600:
		UCA0BR0 = 109;                           // 1.048MHz/9600=109 (see User's Guide)
		UCA0BR1 = 0x00;                          //
		UCA0MCTL |= UCBRS_2  +UCBRF_0;             // Modulation UCBRSx=3, UCBRFx=0
		break;
	case 19200:
		UCA0BR0 = 54;
		UCA0BR1 = 0x00;
		UCA0MCTL |= UCBRS_5 + UCBRF_0;            // Modulation UCBRSx=0, UCBRFx=0
		break;
	case 38400:
		UCA0BR0 = 27;
		UCA0BR1 = 0;
		UCA0MCTL |= UCBRS_2 + UCBRF_0;            // Modulation UCBRSx=0, UCBRFx=0
		break;
	case 57600:
		UCA0BR0 = 18;
		UCA0BR1 = 0;
		UCA0MCTL = UCBRS_1 + UCBRF_0;
		break;
	case 115200:
	default:									//Catch incorrect error
		P4DIR |= BIT7;							// Set on board LED on
		while(1){								// Error trap infinite while loop
			P4OUT ^= BIT7;						// Toggle led
			__delay_cycles(50000);				// Delay
		}
	}
	UCA0CTL1 &= ~UCSWRST;                     // **Initialize USCI state machine**

}
/*\**********************************************************************************************************
 *Function Description
 * 	Transmits one byte over the Serial UART line via the UART debugger
 *Parameters
 *	Byte - information to be sent
 *\**********************************************************************************************************/
void UART_putchar(unsigned char byte){
	while(!(UCA0IFG & UCTXIFG));						//Verify that the line is not busy
	UCA0TXBUF = byte;									//Send byte
}


/*\**********************************************************************************************************
 *Function Description
 * 	Receives one Byte of information from the UART serial line
 *Parameters
 *	Dest - destination were the byte will be stored
 *  mode - 'a' means asynchronous 
 *         'b' means blocking
 *\**********************************************************************************************************/


void UART_getchar(char *dest, char mode){
	if(mode == 'b'){							 // Is in bocking mode?
		char *temp;								 // Temporary storage
		if(!UARTBlock){							 // Was it asynchronous before?
			wasUARTBlock = 1;						 // Indicate it was
			temp = UARTBuff;						 // Save previous location
		}
		UARTBlock = 1;							  // Waits for user input
		UCA0IE |= UCRXIE;                         // Enable USCI_A0 RX interrupt
		UARTBuff = dest;							  // Set receiving location to destination
		LPM0;									  // Wait for interrupt
		if(wasUARTBlock){							  // If it was asynch revert initial conditions
			UARTBlock = 0;						  
			wasUARTBlock = 0;
			UARTBuff = temp;
		}else{
			UCA0IE &= ~UCRXIE;                    // Disable USCI_A0 RX interrupt
			UARTBuff = 0;						  // Clear input register
		}
	}else if(mode == 'a'){
		UARTBlock = 0;							  // Diables blocking
		UARTBuff = dest;							  // Set storage location
		UCA0IE |= UCRXIE;                         // Enable USCI_A0 RX interrupt
	}
}

/*\**********************************************************************************************************
 *Function Description
 * 	Receives one Byte of information from the UART serial line
 *Parameters
 *	Dest - destination were the byte will be stored
 *  mode - 'a' means asynchronous
 *         'b' means blocking
 *  amount - amount of bytes receiving
 *\**********************************************************************************************************/


void UART_getchar_n(char *dest, unsigned int amount, char endian){
	char *temp;								 // Temporary storage
	if(!UARTBlock){							 // Was it asynchronous before?
		wasUARTBlock = 1;						 // Indicate it was
		temp = UARTBuff;						 // Save previous location
	}
	UARTBlock = 1;							  // Waits for user input
	UCA0IE |= UCRXIE;                         // Enable USCI_A0 RX interrupt
	int i;
	UARTBuff = dest;						// Set receiving location to destination

	if(endian == 'b'){
		for(i = amount; i > 0; i--){
			LPM0;									  // Wait for interrupt
			UARTBuff++;
		}
	}else if(endian == 'l'){
		UARTBuff += (amount-1);
		for(i = amount; i > 0; i--){
			LPM0;									  // Wait for interrupt
			UARTBuff--;
		}
	}

	if(wasUARTBlock){						  // If it was asynch revert initial conditions
		UARTBlock = 0;						  //
		wasUARTBlock = 0;
		UARTBuff = temp;
	}else{									  // Wasnt asynchornous - Turn off UART interrups
		UCA0IE &= ~UCRXIE;                    // Disable USCI_A0 RX interrupt
		UARTBuff = 0;						  // Clear input register
	}
}


/*\**********************************************************************************************************
 *Function Description
 * 	Receives an entire line until terminated with a '\0', '\n', or '\r' character
 *Parameters
 *	Dest - destination were the byte will be stored
 *\**********************************************************************************************************/

void UART_getline_b(char *dest){
	char *temp;																						// Temporary holding for old address
	if(!UARTBlock){																					// asynchronous mode active?
		wasUARTBlock = 1;																				// Indicate it was asynchronous
		temp = UARTBuff;																				// Store old location
	}
	UARTBlock = 1;																					 //Waits for input
	UCA0IE |= UCRXIE;																				 // Enable interrupts for this variable
	UARTBuff = dest;																					 // Assign the first value to the array
	LPM0;																							 // Go into low power mode to wait for a byte
	while ((*UARTBuff != '\0') && (*UARTBuff != '\n') && (*UARTBuff != '\r')){							 // While we dont receive a null pointer
		UARTBuff++;					  																 // Increment pointer and assign new value
		LPM0;																						 // Wait for new variable
	}
	*(++UARTBuff) = '\n';																			// Add trailing new line characters
	*(++UARTBuff) = '\r';
	*(++UARTBuff) = '\0';
	if(wasUARTBlock){																					 // Return to asynch mode
		UARTBlock = 0;
		wasUARTBlock = 0;
		UARTBuff = temp;
	}else{
		UCA0IE &= ~UCRXIE;                       													  // Disable USCI_A0 RX interrupt
		UARTBuff = 0;
	}
}



/*\**********************************************************************************************************
 *Function Description
 * 	Prints out a stream of data from the uart line
 *Parameters
 *  String - Character array to be printed
 *\**********************************************************************************************************/
void UART_print(char *string){
	while(*string){							// While there is more content
		UART_putchar(*string);				// Send one byte
		string++;							// Load next byte
	}
}
/*\**********************************************************************************************************
 *Function Description
 * 	Prints out a stream of data from the uart line ending with a new line character
 *Parameters
 *  String - Character array to be printed
 *\**********************************************************************************************************/

void UART_println(char *string){
	UART_print(string);		// Print string
	UART_putchar('\r');		// Append return carrige
	UART_putchar('\n');		// Append new line character
}

/*\**********************************************************************************************************
 *Function Description
 * 	Prints out a stream of data from two data collections
 *Parameters
 *  String1 - Character array to be printed
 *  String2 - Character array to be printed
 *\**********************************************************************************************************/
void UART_print_status(unsigned char *string1,unsigned char *string2){
	while(*string1){					    // While there is more content
		UART_putchar(*string1);				// Send one byte
		string1++;							// Load next byte
	}
	while(*string2){						// While there is more content
		UART_putchar(*string2);				// Send one byte
		string2++;							// Load next byte
	}
}

void UART_print_value(char *string, int value){
	char buffer[16];
	itoa(value, buffer);
	unsigned char *intArr = (unsigned char *)buffer;
	while(*string){
		UART_putchar(*string);
		string++;
	}
	while(*intArr){
		UART_putchar(*intArr);
		intArr++;
	}
}


//UART Interrupt Vector
#pragma vector=USCI_A0_VECTOR
__interrupt void USCI_A0_ISR(void){
	if(UCA0IV == 0x02){						// Receive interrupt
		*UARTBuff = UCA0RXBUF;				// Export to global variable
		if(UARTBlock)
			LPM0_EXIT;							// Exit low power mode
	}
}


/*\**********************************************************************************************************
 * Function Description
 *    Sets up the baud generator for a specific frequency
 * Parameters-
 * 	baudRate - defines the baud rate for communication
 * 		valid frequencies are 9600 and its multiples up to
 * 		115200. Suggested low frequency
 *\**********************************************************************************************************/

char *USBBuff;
char USBBlock;
char wasUSBBlock = 0;

void USB_setup(unsigned long baudRate){
	P4SEL = BIT5+BIT4;                        // P3.4,5 = USCI_A0 TXD/RXD
	//P3REN = BIT3;							// Set up resistor for BT module
	//P3OUT = BIT3;							// Make it pull up
	UCA1CTL1 |= UCSWRST;                      // **Put state machine in reset**
	UCA1CTL1 |= UCSSEL_2;                     // CLK = SUBMAINCLK
	switch(baudRate){
	case 9600:
		UCA1BR0 = 109;                           // 1.048MHz/9600=109 (see User's Guide)
		UCA1BR1 = 0x00;                          //
		UCA1MCTL |= UCBRS_2+UCBRF_0;             // Modulation UCBRSx=3, UCBRFx=0
		break;
	case 19200:
		UCA1BR0 = 54;
		UCA1BR1 = 0x00;
		UCA1MCTL |= UCBRS_5 +UCBRF_0;            // Modulation UCBRSx=0, UCBRFx=0
		break;
	case 38400:
		UCA1BR0 = 27;
		UCA1BR1 = 0;
		UCA1MCTL |= UCBRS_2 +UCBRF_0;            // Modulation UCBRSx=0, UCBRFx=0
		break;
	case 57600:
		UCA1BR0 = 18;
		UCA1BR1 = 0;
		UCA1MCTL = UCBRS_1 + UCBRS_0;
		break;
	case 115200:
	default:									//Catch incorrect error
		P4DIR |= BIT7;							// Set on board LED on
		while(1){								// Error trap infinite while loop
			P4OUT ^= BIT7;						// Toggle led
			__delay_cycles(50000);				// Delay
		}
	}
	UCA1CTL1 &= ~UCSWRST;                     // **Initialize USCI state machine**
}
/*\**********************************************************************************************************
 *Function Description
 * 	Transmits one byte over the Serial UART line via the USB debugger
 *Parameters
 *	Byte - information to be sent
 *\**********************************************************************************************************/
void USB_putchar(unsigned char byte){
	while(!(UCA1IFG & UCTXIFG));						//Verify that the line is not busy
	UCA1TXBUF = byte;									//Send byte
}


/*\**********************************************************************************************************
 *Function Description
 * 	Receives one Byte of information from the UART serial line
 *Parameters
 *	Dest - destination were the byte will be stored
 *  mode - 'a' means asynchronous
 *         'b' means blocking
 *\**********************************************************************************************************/


void USB_getchar(char *dest, char mode){
	if(mode == 'b'){							 // Is in bocking mode?
		char *temp;								 // Temporary storage
		if(!USBBlock){							 // Was it asynchronous before?
			wasUSBBlock = 1;						 // Indicate it was
			temp = USBBuff;						 // Save previous location
		}
		USBBlock = 1;							  // Waits for user input
		UCA1IE |= UCRXIE;                         // Enable USCI_A0 RX interrupt
		USBBuff = dest;							  // Set receiving location to destination
		LPM0;									  // Wait for interrupt
		if(wasUSBBlock){							  // If it was asynch revert initial conditions
			USBBlock = 0;
			wasUSBBlock = 0;
			USBBuff = temp;
		}else{
			UCA1IE &= ~UCRXIE;                    // Disable USCI_A0 RX interrupt
			USBBuff = 0;						  // Clear input register
		}
	}else if(mode == 'a'){
		USBBlock = 0;							  // Diables blocking
		USBBuff = dest;							  // Set storage location
		UCA1IE |= UCRXIE;                         // Enable USCI_A0 RX interrupt
	}
}



/*\**********************************************************************************************************
 *Function Description
 * 	Receives one Byte of information from the UART serial line
 *Parameters
 *	Dest - destination were the byte will be stored
 *  mode - 'a' means asynchronous
 *         'b' means blocking
 *  amount - amount of bytes receiving
 *\**********************************************************************************************************/


void USB_getchar_n(char *dest, unsigned int amount){
	char *temp;								 // Temporary storage
	if(!USBBlock){							 // Was it asynchronous before?
		wasUSBBlock = 1;						 // Indicate it was
		temp = USBBuff;						 // Save previous location
	}
	USBBlock = 1;							  // Waits for user input
	UCA1IE |= UCRXIE;                         // Enable USCI_A0 RX interrupt
	int i;
	USBBuff = dest;							  // Set receiving location to destination
	for(i = amount; i > 0; i--){
		LPM0;									  // Wait for interrupt
		USBBuff++;
	}
	if(wasUSBBlock){							  // If it was asynch revert initial conditions
		USBBlock = 0;
		wasUSBBlock = 0;
		USBBuff = temp;
	}else{
		UCA1IE &= ~UCRXIE;                    // Disable USCI_A0 RX interrupt
		USBBuff = 0;						  // Clear input register
	}
}

/*\**********************************************************************************************************
 *Function Description
 * 	Receives an entire line until terminated with a '\0', '\n', or '\r' character
 *Parameters
 *	Dest - destination were the byte will be stored
 *\**********************************************************************************************************/

void USB_getline_b(char *dest){
	char *temp;																						// Temporary holding for old address
	if(!USBBlock){																					// asynchronous mode active?
		wasUSBBlock = 1;																				// Indicate it was asynchronous
		temp = USBBuff;																				// Store old location
	}
	USBBlock = 1;																					 //Waits for input
	UCA1IE |= UCRXIE;																				 // Enable interrupts for this variable
	USBBuff = dest;																					 // Assign the first value to the array
	LPM0;																							 // Go into low power mode to wait for a byte
	while ((*USBBuff != '\0') && (*USBBuff != '\n') && (*USBBuff != '\r')){							 // While we dont receive a null pointer
		USBBuff++;					  																 // Increment pointer and assign new value
		LPM0;																						 // Wait for new variable
	}
	*(++USBBuff) = '\n';																			// Add trailing new line characters
	*(++USBBuff) = '\r';
	*(++USBBuff) = '\0';
	if(wasUSBBlock){																					 // Return to asynch mode
		USBBlock = 0;
		wasUSBBlock = 0;
		USBBuff = temp;
	}else{
		UCA1IE &= ~UCRXIE;                       													  // Disable USCI_A0 RX interrupt
		USBBuff = 0;
	}
}



/*\**********************************************************************************************************
 *Function Description
 * 	Prints out a stream of data from the uart line
 *Parameters
 *  String - Character array to be printed
 *\**********************************************************************************************************/
void USB_print(char *string){
	while(*string){							// While there is more content
		USB_putchar(*string);				// Send one byte
		string++;							// Load next byte
	}
}
/*\**********************************************************************************************************
 *Function Description
 * 	Prints out a stream of data from the uart line ending with a new line character
 *Parameters
 *  String - Character array to be printed
 *\**********************************************************************************************************/

void USB_println(char *string){
	USB_print(string);		// Print string
	USB_putchar('\r');		// Append return carrige
	USB_putchar('\n');		// Append new line character
}

/*\**********************************************************************************************************
 *Function Description
 * 	Prints out a stream of data from two data collections
 *Parameters
 *  String1 - Character array to be printed
 *  String2 - Character array to be printed
 *\**********************************************************************************************************/
void USB_print_status(unsigned char *string1,unsigned char *string2){
	while(*string1){					    // While there is more content
		USB_putchar(*string1);				// Send one byte
		string1++;							// Load next byte
	}
	while(*string2){						// While there is more content
		USB_putchar(*string2);				// Send one byte
		string2++;							// Load next byte
	}
}

void USB_print_value(char *string, int value){
	char buffer[16];
	itoa(value, buffer);
	unsigned char *intArr = (unsigned char *)buffer;
	while(*string){
		USB_putchar(*string);
		string++;
	}
	while(*intArr){
		USB_putchar(*intArr);
		intArr++;
	}
}


//UART Interrupt Vector
#pragma vector=USCI_A1_VECTOR
__interrupt void USCI_A1_ISR(void){
	if(UCA1IV == 0x02){						// Receive interrupt
		*USBBuff = UCA1RXBUF;				// Export to global variable
		if(USBBlock)
			LPM0_EXIT;							// Exit low power mode
	}
}


///// END OF USB
////////////////////////////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////////////////////////////
///// I2C Functionality
unsigned char txAddress;
unsigned char *txData;
unsigned char *rxDest;
unsigned char rxByteCtr;
unsigned int txByteCtr;
unsigned int txLength;
unsigned int rx;
#define DELAY 100
/*\***********************************************************************************************************
 *Function Description
 * 	Bootstrap for the I2C serial bus on UCB0
 *Parameter description
 *  Baud rate - defines the synchronous clock rate to be utilized
 *  slaveAddress - defines the slave address that the slave will use
 *
 *\************************************************************************************************************/
void I2C_setup(unsigned long baudRate){

	P3SEL |= 0x03;                            // Assign I2C pins to USCI_B0
	UCB0CTL1 |= UCSWRST;                      // Enable SW reset
	UCB0CTL0 = UCMST + UCMODE_3 + UCSYNC;     // I2C, Master, synchronous mode
	UCB0CTL1 = UCSSEL_2 + UCSWRST;            // Use SMCLK, keep SW reset
	if(baudRate == 10000){
		UCB0BR0 = 105;                          // fSCL = SMCLK/105 = ~10kHz
		UCB0BR1 = 0;
	}if(baudRate == 100000){
		UCB0BR0 = 105;                          // fSCL = SMCLK/12 = ~100kHz
		UCB0BR1 = 0;
	}if(baudRate == 400000){
		UCB0BR0 = 3;
		UCB0BR1 = 0;
	}
	UCB0CTL1 &= ~UCSWRST;                     // Clear SW reset, resume operation
	UCB0IE |= UCRXIE + UCTXIE;                // Enable interrupts
}
/*\**********************************************************************************************************
 *Function Description
 *	 Writes a stream of data to an I2C bus
 *Parameters
 * 	 Slave Address - Address of the slave to receive data
 * 	 Register Address - Internal register of the slave to access
 * 	 Data pointer - Byte or collection of consecutive bytes to write to the slave
 * 	 Amount - Amount of bytes to send
 *\\**********************************************************************************************************/




void I2C_write(unsigned char slaveAddress, unsigned char registerAddress, unsigned char *data, unsigned int length){
	_BIC_SR(GIE);
	rx = 0x00;
	txByteCtr = length;						// Set global variable
	txLength = length;
	txAddress = registerAddress;			// Set global variable
	txData = data;
	UCB0I2CSA = slaveAddress;               // Slave Address
	while (UCB0CTL1 & UCTXSTP);             // Ensure stop condition got sent
	UCB0CTL1 |= UCTR + UCTXSTT;             // I2C TX, start condition
	__bis_SR_register(LPM0_bits + GIE);     // Enter LPM0 w/ interrupts
}

/*\***********************************************************************************************************
 *Function Description
 * 	Reads a stream of data from an I2C Slave
 *Parameter description
 *  Slave Address - Address of the slave to access
 * 	Register Address - Internal register of the slave to access
 * 	Read Destination - pointer to the variable in memory to store
 * 	Length - amount of bytes to dump onto the read destination
 *\***********************************************************************************************************/


void I2C_read(unsigned char slaveAddress, unsigned char registerAddress, unsigned char *readDestination, unsigned int length){
	I2C_write(slaveAddress, registerAddress, 0, 0);		// Send slave device register address
	__bic_SR_register(GIE);								// Clear interrupts just in case
	rx = 0xFF;
	rxByteCtr = length;									// Set global variable
	rxDest = readDestination;							// Pass along the destination of the read
	while (UCB0CTL1 & UCTXSTP);             			// Ensure stop condition got sent
	UCB0CTL1 &= ~UCTR;                     			// Clear UCTR
	UCB0CTL1 |= UCTXSTT;                    			// I2C start condition
	if(rxByteCtr == 1){									// Only receiving one byte?
		while (UCB0CTL1 & UCTXSTT);         			// Start condition sent?
		UCB0CTL1 |= UCTXSTP;                			// I2C stop condition
	}
	__bis_SR_register(LPM0_bits + GIE);     			// Enter LPM0 w/ interrupts
}

/*\***********************************************************************************************************
 *Function Description
 * 	I2C Interrupt function to handle data amount
 *Parameter description
 *  Baud rate - defines the synchronous clock rate to be utilized
 *
 *\************************************************************************************************************/
#pragma vector = USCI_B0_VECTOR
__interrupt void USCI_B0_ISR(void){
	switch(__even_in_range(UCB0IV, 12)){
	case 2:												// NACK IFG
		UCB0CTL1 |= UCTXSTP;			    			// Send stop condition
		UCB0IFG &= ~UCRXIFG;							// Clear any mistaken flag
		__bic_SR_register_on_exit(LPM0_bits);			// Exit low power mode
		break;

	case 10: // RxIFG - Receive interrupt condition
		if(rx){
			rxByteCtr--;									// Decrease Rx counter
			if(rxByteCtr){									// More than 1 value left
				*rxDest++ = UCB0RXBUF;						// Receive into memory
				if(rxByteCtr == 1){							// One byte left
					__delay_cycles(DELAY);
					UCB0CTL1 |= UCTXSTP;					// Initiate stop after next byte read
				}
			}else{											// Last byte to read
				*rxDest = UCB0RXBUF;						// Allocate in memory
				UCB0IFG &= ~UCRXIFG;						// Clear any mistaken flag
				__bic_SR_register_on_exit(LPM0_bits);		// Exit low power mode
			}
		}
	case 12: 											    // TxIFG - Receive interrupt condition
		if(!rx){
			if(txByteCtr == txLength){						// Check if its the first transmission
				UCB0TXBUF = txAddress;						// Send the slave device register to write or read
				if (txLength == 0){							// Verify if only sending register address
					__delay_cycles(DELAY);
					UCB0CTL1 |= UCTXSTP;					// Send stop condition
					UCB0IFG &= ~UCTXIFG;					// Clear interrupt in (missfire check)
					__bic_SR_register_on_exit(LPM0_bits);	// Exit low power mode - concludes transmission
				}
				txLength++;									// Invalidate conditional to avoid looping in
				break;
			}else if(txByteCtr > 0){						// More than 1 byte left to send?
				UCB0TXBUF = *txData++;						// Send next byte and increase pointer directive
				txByteCtr--;								// Decrease amount of bytes left to send
			}else{											// Last byte to be sent
				UCB0TXBUF = *txData;						// Send last byte
				__delay_cycles(DELAY);
				UCB0CTL1 |= UCTXSTP;						// Send stop condition
				UCB0IFG &= ~UCTXIFG;						// Clear interrupt in (missfire check)
				__bic_SR_register_on_exit(LPM0_bits);		// Exit low power mode - concludes transmission
			}
		}
	default: break;
	}
}
///// END OF I2C
////////////////////////////////////////////////////////////////////////////////////////////////////////
