/*
 * MS5837-30BA.h
 *
 *  Created on: Dec 22, 2016
 *      Author: RathK
 */

#ifndef MS5837_30BA_H_
#define MS5837_30BA_H_

void PRESSURE_calibrate();
void PRESSURE_start_conversion();
int32 PRESSURE_get_pressure();
int32 PRESSURE_get_temperature();


int feet_to_Bar(int feet);


#endif /* MS5837_30BA_H_ */
