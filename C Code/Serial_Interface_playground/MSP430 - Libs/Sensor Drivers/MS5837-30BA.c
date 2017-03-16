#include <msp430.h> 
#include "Serial_JMP.h"
#include "General_JMP.h"
#include "typecast.h"
#include "MS5837-30BA.h"
/*
 * Created by Jose A. Montes Perez
 * Algorithm taken from  [1] MS5837-30BA datasheet - page 7
 * [1] http://www.mouser.com/ds/2/418/MS5837-30BA-736494.pdf
 *
 */

//Data sheet variables
//Variable names taken straight from datasheet
uint16 C1; //Pressure Sensitivity
uint16 C2; //Pressure Offset
uint16 C3; //Temperature coefficient of pressure sensitivity
uint16 C4; //Temperature coefficient of pressure offset
uint16 C5; //Reference temperature
uint16 C6; //Temperature coefficient of the temperature

uint32 D1; //Digital pressure value
uint32 D2; //Digital temperature value

int32 dT; //Difference between actual and reference value
int32 TEMP; //Actual temperature

int32 OFF; //Offset actual temperature
int32 SENS; //Sensitivity at actual temperature
int32 P; //Temperature compensated pressure


#define CONVERSION_TIME 5
#define CONVERSION_CYCLES 5240
//I2C Addresses
#define PSENSOR 0x76


//Commands list for the pressure sensor
#define RESET 0x1E
#define CONVERT_D1 0x46
#define CONVERT_D2 0x56
#define ADC_READ 0x00
#define PROM_READ_C1 0xA2
#define PROM_READ_C2 0xA4
#define PROM_READ_C3 0xA6
#define PROM_READ_C4 0xA8
#define PROM_READ_C5 0xAA
#define PROM_READ_C6 0xAC

//Local dependencies
unsigned char I2C_buffer[8];

/*
 * Function description
 * Force a POR on the pressure sensor to ensure
 * accurate data on the calibration registers
 *
 */
void reset_sequence(){
	I2C_write(PSENSOR, RESET, 0, 0);	//Send reset command to the pressure sensor
	__delay_cycles(5000);
}
/*
 * Function description
 * This reads the factory calibration registers and stores it in
 * the C1 - C6 variables
 *
 */


void read_factory_calibration(){
	I2C_read(PSENSOR, PROM_READ_C1, &I2C_buffer[0], 2);
	C1 = (I2C_buffer[0] << 8) | I2C_buffer[1];
	I2C_read(PSENSOR, PROM_READ_C2, &I2C_buffer[0], 2);
	C2 = (I2C_buffer[0] << 8) | I2C_buffer[1];
	I2C_read(PSENSOR, PROM_READ_C3, &I2C_buffer[0], 2);
	C3 = (I2C_buffer[0] << 8) | I2C_buffer[1];
	I2C_read(PSENSOR, PROM_READ_C4, &I2C_buffer[0], 2);
	C4 = (I2C_buffer[0] << 8) | I2C_buffer[1];
	I2C_read(PSENSOR, PROM_READ_C5, &I2C_buffer[0], 2);
	C5 = (I2C_buffer[0] << 8) | I2C_buffer[1];
	I2C_read(PSENSOR, PROM_READ_C6, &I2C_buffer[0], 2);
	C6 = (I2C_buffer[0] << 8) | I2C_buffer[1];
}

void read_conversions(){
	I2C_write(PSENSOR, CONVERT_D1, 0, 0);					// Initialize conversion
	__delay_cycles(CONVERSION_CYCLES);												// Wait 20ms (worst case) for conversion to end
	I2C_read(PSENSOR, ADC_READ, &I2C_buffer[0], 3);
	D1 = ((uint32) I2C_buffer[0] << 16) | ((uint32) I2C_buffer[1] << 8) | I2C_buffer[3];
	I2C_write(PSENSOR, CONVERT_D2, 0, 0);					// Initialize conversion
	__delay_cycles(CONVERSION_CYCLES);											// Wait 20ms (worst case) for conversion to end
	I2C_read(PSENSOR, ADC_READ, &I2C_buffer[0], 3);
	D2 = ((uint32) I2C_buffer[0] << 16) | ((uint32) I2C_buffer[1] << 8) | I2C_buffer[3];
}
/*
 * Function test description
 * This gives basic values to compare your read data from
 *
 *
 *
 */
void test_case() {

	C1 = 34982;
	C2 = 36352;
	C3 = 20328;
	C4 = 22354;
	C5 = 26646;
	C6 = 26146;

	D1 = 4958179;
	D2 = 6815414;

}
/*
 * Function description
 *
 *
 *
 *
 */
void calculate_pressure(){

	// First order conversion
	dT = D2 - (uint32) (C5 << 8);
	TEMP = 2000 + ((dT* (uint32) C6) >> 23);

	OFF = ((uint32) C2 << 16) + ((((uint32)C4)*dT) >> 7);
	SENS =  (((uint32) C1) << 15) + ((((int32) C3)*dT) >> 8);
	//P = ((((uint64)D1*SENS)>>21) - OFF) >> 13;

	//Second order conversion
	int32 SENSi;
	int32 OFFi;
	int64 Ti;
	int64 OFF2;
	int64 SENS2;


	if(TEMP < 2000){
		Ti = (3*(int64)dT*(int64)dT)>> 33;
		OFFi = 3*(TEMP=2000)*(TEMP-2000) >> 1;
		SENSi = 5*(TEMP=2000)*(TEMP-2000) >> 3;
		if (TEMP < -1500){
			OFFi = OFFi + 7*(TEMP+1500)*(TEMP+1500);
			SENSi = SENSi + 4*(TEMP + 1500)*(TEMP + 1500);
		}
	}else{
		Ti = ((2*(int64) (dT)*(int64)(dT)) >> 37);
		OFFi = (TEMP-2000)*(TEMP-2000) >> 4;
		SENSi = 0;
	}
	OFF2 = OFF - OFFi;
	SENS2 = SENS - SENSi;

	//TEMP = (TEMP - Ti);
	P = ((((uint64)D1*SENS2)>>21) - OFF2) >> 13;
}
int feet_to_Bar(int feet){
	return 299*feet;
}
/*
 * Function description
 * Initializes the sensor
 *
 */

void PRESSURE_calibrate(){
	reset_sequence();
	read_factory_calibration();
}
/*
 * Function descriptions
 * Starts the conversion for the Pressure and temperature
 *
 *
 */
void PRESSURE_start_conversion(){
	read_conversions();
	calculate_pressure();
}

/*
 * Function description
 * Gets the last Pressure reading
 *
 */
int32 PRESSURE_get_pressure(){
	return P;
}
/*
 * Function description
 * Gets the last temperature reading
 *
 */
int32 PRESSURE_get_temperature(){
	return TEMP;
}


/* Fucntioning test case
int main(void) {
    WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer
    _BIS_SR(GIE);
	I2C_setup(400000);			//Start I2C communication at 100k bps
	USB_setup(9600);

	reset_sequence();
	read_factory_calibration();


	while(1){
		read_conversions();
		//test_case();

		calculate_pressure();
		_no_operation();
		USB_print_value("Pressure is: ", P);
		USB_print_value("     Temperature is: ", TEMP);
		USB_print("\r\n");
	}
}
*/

