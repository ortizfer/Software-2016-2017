/*
 * General_JMP.h
 *
 *  Created on: Oct 26, 2016
 *      Author: jose.montes1
 */

#ifndef GENERAL_JMP_H_
#define GENERAL_JMP_H_


#define abss(a) a > 0 ? a : -1*a
#define sign(a) a > 0 ? 1 : -1

void interrupts(char on);
void delay(unsigned long miliSeconds);
void delaySeconds(unsigned long miliseconds);
void timeExceed(int seconds, unsigned char *dest);
void inline startDelay();
void inline stopDelay();
__interrupt void TIMER_B0(void);

void reverse(char s[]);
void itoa(int n, char s[]);

#endif /* GENERAL_JMP_H_ */
