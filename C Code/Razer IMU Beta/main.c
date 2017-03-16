#include <msp430.h> 
#include "Serial_JMPv2.0.h"
#include "Razor_AHRS.h"
#include "General_JMP.h"

/*
 * Created by Jose A. Montes Perez
 * 	On Dec 21, 2016
 *
 * This code is designed to interface the
 * sparkfun RAzor 9dog IMU[1] with the msp430f559lp.
 * The code is inspired via the firmware found in [2].
 *
 * Depends on Serial_JMP.h
 *
 * Wiring diagram:
 * P3.3 -> TX@Razor
 * P3.4 -> RX@Razor
 *
 * USB -> PC COM PORT
 *
 * [1]https://www.sparkfun.com/products/retired/10736
 * [2]https://github.com/Razor-AHRS/razor-9dof-ahrs
 *
 *
 *
 */


void main(void) {
	WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer
	RAZOR_sngl_setup();
	RAZOR_out_angles();
	_BIS_SR(GIE);
	volatile float n_yaw,n_pitch,n_roll, lol;
	lol = 0;
	RAZOR_refresh_value();
	n_yaw = yaw;
	n_pitch = pitch;
	n_roll = roll;
	while(1){
		RAZOR_refresh_value();
		lol = n_yaw + n_pitch + n_roll;
		n_yaw = yaw;
		n_pitch = pitch;
		n_roll = roll;
		__delay_cycles(20000);
	}
}

