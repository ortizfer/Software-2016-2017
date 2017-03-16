#ifndef LCD_JMP_H_
#define LCD_JMP_H_

#define aclk_frq 32768
#define E_high P2OUT |= 0x04 //ENABLE PIN HIGH
#define E_low P2OUT &= ~0x04 //ENABLE PIN LOW
#define RS_high P2OUT |= 0x01 //ENABLE PIN HIGH
#define RS_low P2OUT &= ~0x01 //ENABLE PIN LOW

void write(char data);
void write_str(char *str);
void cursor_top();
void cursor_bot();
void clear_lcd();
void lcdInit();

#endif /* LCD_JMP_H_ */