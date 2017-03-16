/*
 * Serial_JMP.h
 *
 *  Created on: Oct 25, 2016
 *      Author: Rathk
 */

#ifndef SERIAL_JMP_H_
#define SERIAL_JMP_H_

#define SUCCESS "\n\rProcess successful: "
#define FAIL "\n\rProcess failed: "


void UART_setup(unsigned long baudRate);
void UART_transmit_byte(unsigned char byte);
void UART_receive_byte(char *dest);
void UART_print(char *string);
void UART_println(char *string);
void UART_print_status(unsigned char *string1,unsigned char *string2);
void UART_print_value(char *string, int value);
__interrupt void USCI_A0_ISR(void);

void USB_setup(unsigned long baudRate);
void USB_transmit_byte(unsigned char byte);
void USB_receive_byte(char *dest);
void USB_print(char *string);
void USB_println(char *string);
void USB_print_status(unsigned char *string1,unsigned char *string2);
void USB_print_value(char *string, int value);
__interrupt void USCI_A1_ISR(void);

void I2C_setup(unsigned long baudRate);
void I2C_write(unsigned char slaveAddress, unsigned char registerAddress, unsigned char *data, unsigned int length);
void I2C_read(unsigned char slaveAddress, unsigned char registerAddress, unsigned char *readDestination, unsigned int length);
__interrupt void USCI_B0_ISR(void);


void BT_timeout_setup(int miliseconds);
void BT_restart_timeout();
void BT_stop_timeout();

volatile char BT;

void SAMPLE_measure();
void SAMPLE_enable_interrupt();
__interrupt void TIMER1_A0_ISR(void);

#endif /* SERIAL_JMP_H_ */
