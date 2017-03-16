/*
 * Sampling_JMP.c
 *
 *  Created on: Mar 2, 2017
 *      Author: Jose A. Montes Perez
 */




/*\***********************************************************************************************************
 *Function Description
 * 	Sets up s fucntion to timeout the system in case it gets stuck in an open loop.
 *Parameter description
 *  	miliseconds - the miliseconds the function will wait before continuing.
 *
 *\************************************************************************************************************/

void BT_timeout_setup(int miliseconds){
	unsigned long operations = (32768*miliseconds)/1000;
	TA1CTL |= TBCLR; 				// Clear Timer content and settup
	TA1CCR0 = operations;			// Set the timer period
	TA1CTL |= TBSSEL_1;			    // Use aclk
	TA1CCTL0 |= CCIE;				// Enable Interrupt
}

/*\***********************************************************************************************************
 *Function Description
 * 	Restarts the timeout to wait the allloted time given in teh setup
 *Parameter description
 *
 *
 *\************************************************************************************************************/

void BT_restart_timeout(){
	BT = 1;
	TA1R = 0;					// Reset Counter
	TA1CTL |= MC_1;			    // Use up mode
}

/*\***********************************************************************************************************
 *Function Description
 * 	Stops the timeout after the function you want is completed.
 *Parameter description
 *
 *
 *\************************************************************************************************************/

void BT_stop_timeout(){
	TA1CTL &= ~MC_1;				//Stop timer
}


void SAMPLE_enable_interrupt(){
	BT = 0;
	TA1R = 0;					// Reset Counter
	TA1CTL |= MC_1;			    // Use up mode
}



/*\***********************************************************************************************************
 *Function Description
 * 	Interrupt service routine to sevice the timout function
 *Parameter description
 *
 *
 *\************************************************************************************************************/

#pragma vector=TIMER1_A0_VECTOR
__interrupt void TIMER0_A1_ISR(void){
	if(!BT){
		SAMPLE_measure();
	}else{
		TA1CTL &= ~MC_1;				//Stop timer
		TA1CTL |= MC_0;					//Make sure its stopped
		LPM0_EXIT;
	}
}

