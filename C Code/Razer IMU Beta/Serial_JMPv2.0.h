/*
 * Serial_JMP.h
 *
 *  Created on: Oct 25, 2016
 *      Author: Jose A. Montes
 */

#ifndef SERIAL_JMP_H_
#define SERIAL_JMP_H_

#define SUCCESS "\n\rProcess successful: "
#define FAIL "\n\rProcess failed: "

#define USB_getchar_b(a) USB_getchar(a, 'b')
#define USB_getchar_a(a) USB_getchar(a, 'a')
#define UART_getchar_b(a) UART_getchar(a, 'b')
#define UART_getchar_a(a) UART_getchar(a, 'a')


void UART_setup(unsigned long baudRate);
void UART_putchar(unsigned char byte);
void UART_getchar(char *dest, char mode);
void UART_getchar_n(char *dest, unsigned int amount, char endian);
void UART_getline_b(char *dest);

//char UART_transmission_complete(); - implement asynchronous getline and getchar_n via counter and this method

void UART_print(char *string);
void UART_println(char *string);
void UART_print_status(unsigned char *string1,unsigned char *string2);
void UART_print_value(char *string, int value);
__interrupt void USCI_A0_ISR(void);

void USB_setup(unsigned long baudRate);
void USB_putchar(unsigned char byte);
void USB_getchar(char *dest, char mode);
void USB_getchar_n(char *dest, unsigned int amount);
void USB_getline_b(char *dest);
void USB_print(char *string);
void USB_println(char *string);
void USB_print_status(unsigned char *string1,unsigned char *string2);
void USB_print_value(char *string, int value);
__interrupt void USCI_A1_ISR(void);

void I2C_setup(unsigned long baudRate);
void I2C_write(unsigned char slaveAddress, unsigned char registerAddress, unsigned char *data, unsigned int length);
void I2C_read(unsigned char slaveAddress, unsigned char registerAddress, unsigned char *readDestination, unsigned int length);
__interrupt void USCI_B0_ISR(void);


#endif /* SERIAL_JMP_H_ */
