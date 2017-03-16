/*
 * General_JMP.h
 *
 *  Created on: Oct 26, 2016
 *      Author: jose.montes1
 */

#ifndef GENERAL_JMP_H_
#define GENERAL_JMP_H_


#define aclk_frq 32768
#define E_high P2OUT |= 0x04 //ENABLE PIN HIGH
#define E_low P2OUT &= ~0x04 //ENABLE PIN LOW
#define RS_high P2OUT |= 0x01 //ENABLE PIN HIGH
#define RS_low P2OUT &= ~0x01 //ENABLE PIN LOW

void interrupts(char on);
void delay(unsigned long miliSeconds);
//__interrupt void TIMER_B0(void);
void command(char cmd);
void write(char data);
void write_str(char *str);
void cursor_top();
void cursor_bot();
void clear_lcd();
void lcdInit();
void reverse(char s[]);
void itoa(int n, char s[]);

#endif /* GENERAL_JMP_H_ */
