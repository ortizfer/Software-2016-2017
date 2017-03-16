#include <stdio.h>
/*
 * Fuzzy logic control engine
 * Made by:
 * Jose A. Montes Perez
 *
 * Rudimentary control engine utiliaing the
 * Sugeno Zero Order fuzzy logic control scheme
 *
 * User guide to be made
 */

#define MEMBERSHIP_SCALING 255
#define NUMBER_OF_INPUTS 10
#define NUMBER_OF_OUTPUTS 10


#define MAX(A,B) (A > B) ? A : B
#define MIN(A,B) (A < B) ? A : B


//Defines a single input variable and its defuzzification
typedef struct FIS_input{
	 int input;
	 int (*fuzzify)(int input);
	 unsigned char amountOfInputs;
}FIS_input;


//Defines the output singleton spikes
typedef struct FIS_output{
	int outputVals[NUMBER_OF_OUTPUTS];
	unsigned char amountOfOutputs;
}FIS_output;

//Defines a single rule
typedef struct FIS_rule{
	signed char input[NUMBER_OF_INPUTS];				//1 applies AND, -1 applies OR, 0 skips variable in order of inputed variables
	signed char output[NUMBER_OF_INPUTS];				//1 applies AND, -1 applies OR, 0 skips variables in order of inputted outputs
	unsigned char amountOfRules;					//amount of rules
}FIS_rule;


//void FIS_update_inputs();


char FIS_fuzzify_input(FIS_input *vars){
	return vars->fuzzify(vars->input);

}

int FIS_apply_antecedent( char fuzzyInput[], int amountOfInputs, FIS_rule *rule){
	unsigned int i = 0; 																						// Local Counter
	unsigned int first;																						// First valid condition found
	int ruleInput = 0;																				// Antecedent ouput local variable
	while(rule->input[i] == 0 && i < amountOfInputs)													// Loop until you find the first valid input
		i++;
	first = i;																						// Store first location
	if( i > amountOfInputs)																			// If no location found return 0
		return 0;
	while(rule->input[i] == 0 && i < amountOfInputs)													// Loop until you find second valid location
		i++;
	if ( i > amountOfInputs)																		// If no other location found return the first input
		ruleInput = rule->input[first];
	else {																							// Else - two location have been found
		switch(rule->input[i]){																		// Fix output for inital case
			case 1: ruleInput=MAX(fuzzyInput[first], fuzzyInput[i]);break;
			case -1: ruleInput = MIN(fuzzyInput[first], fuzzyInput[i]);break;
			case 0: break;
			default: break;
		}
	}
	for ( ; i < amountOfInputs; i++){																// Is there another rule to be applied?
		switch(rule->input[i]){
			case 1: ruleInput = MAX(ruleInput, fuzzyInput[i]);break;
			case -1: ruleInput = MIN(ruleInput, fuzzyInput[i]);break;
			case 0: break;
			default: break;
		}
	}
	return ruleInput;
}

int FIS_apply_implication(int antecedent, FIS_rule *rule, int amountOfOutputs, int outputVals[]){
	//Implication process
	unsigned int i = 0;
	unsigned int first = 0;
	int ruleOutput;
	while(rule->output[i] == 0 && i < amountOfOutputs)
		i++;
	first = i;
	if( i > amountOfOutputs)
		return 0;
	while(rule->output[i] == 0 && i < amountOfOutputs)
		i++;
	if ( i > amountOfOutputs)
		return antecedent*outputVals[first];
	switch(rule->output[i]){
			case 1: ruleOutput = MAX(outputVals[first], outputVals[i]);break;
			case -1: ruleOutput = MIN(outputVals[first], outputVals[i]);break;
			case 0: break;
			default: break;
	}
	for ( ; i < amountOfOutputs; i++){
		switch(rule->output[i]){
			case 1: ruleOutput = MAX(ruleOutput, outputVals[i]);break;
			case -1: ruleOutput = MIN(ruleOutput, outputVals[i]);break;
			case 0: break;
			default: break;
		}
	}
	return ruleOutput*antecedent;
}


int FIS_defuzzify_output(int agregate, int amountOfRules){
	return agregate/amountOfRules/MEMBERSHIP_SCALING;
}


//Do - FIS_update_variables() first
int FIS_engine(FIS_input *vars[], FIS_rule *rules[], FIS_output *out){
	unsigned int agregate = 0;
	unsigned int i = vars[0]->amountOfInputs;
	unsigned int j = rules[0]->amountOfRules;
	char fuzzyInputs[i];

	for ( ; i > 0; --i){
		fuzzyInputs[i] = FIS_fuzzify_input(vars[i]);
	}
	int buff;
	for ( ; j > 0; --j){
		buff = FIS_apply_antecedent(fuzzyInputs, i, rules[j]);
		agregate += FIS_apply_implication(buff, rules[j], out->amountOfOutputs, out->outputVals);
	}
	buff = FIS_defuzzify_output(agregate, rules[0]->amountOfRules);
	return buff;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TEST AREA //////////////////////////////////////////////////////////////////////////////////////////////////////////////
int membership_poor(int input){
	if(input > 4){
		return 0;
	}else{
		return MEMBERSHIP_SCALING - (MEMBERSHIP_SCALING*input>>2);
	}
}
int membership_good(int input){
	if(input < 2){
		return MEMBERSHIP_SCALING/12*input;
	}else if (input <= 2 && input < 5){
		return MEMBERSHIP_SCALING*5/18*input - 7/18*MEMBERSHIP_SCALING;
	}else if (input <= 5 && input < 8){
		return 43/18*MEMBERSHIP_SCALING - MEMBERSHIP_SCALING*5/18*input;
	}else{
		return MEMBERSHIP_SCALING/12 - MEMBERSHIP_SCALING/24*(8-input);
	}
}

int membership_great(int input){
	if(input < 6){
		return 0;
	}else{
		return (MEMBERSHIP_SCALING/4*(input - 5));
	}
}

int membership_rancid(int input){
	if(input < 1){
		return MEMBERSHIP_SCALING;
	}else if(input < 4){
		return MEMBERSHIP_SCALING - MEMBERSHIP_SCALING/2*(input - 1);
	}else{
		return 8;
	}
}

int membership_delicious(int input){
	if(input < 7){
		return 0;
	}else if(input >= 7){
		return MEMBERSHIP_SCALING*2*(input - 7);
	}else{
		return MEMBERSHIP_SCALING;
	}
}



FIS_input servicePoor = { 0, *membership_poor, 5};
FIS_input serviceGood = {0, *membership_good, 5};
FIS_input serviceGreat = {0, *membership_great, 5};
FIS_input foodRancid = {0, *membership_rancid, 5};
FIS_input foodDelicious = {0, *membership_delicious, 5};

FIS_input *vars[5] = {&servicePoor, &serviceGood, &serviceGreat, &foodRancid, &foodDelicious};


FIS_rule rule1 = {{1,0,0,-1,0}, {1,0,0}, 3};
FIS_rule rule2 = {{0,1,0,0,0},  {0,1,0}, 3};
FIS_rule rule3 = {{0,0,1,0,-1}, {0,0,1}, 3};

FIS_rule *rules[3] = {&rule1, &rule2, &rule3};

FIS_output out = { {5,15,25}, 3};

FIS_update_inputs(int service, int food){
	servicePoor.input = service;
	serviceGood.input = service;
	serviceGreat.input = service;
	foodRancid.input = food;
	foodDelicious.input = food;
}



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\\
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\\\

int main(void) {
	int service, food, buff;
	printf("Input service quality: ");
	scanf("%d", &service);
	printf("Input food quality: ");
	scanf("%d", &food);
	printf("testing/n");

	FIS_update_inputs(service, food);
	buff = FIS_engine(vars, rules, &out);
	printf("Drumrolll: %d", buff);

	return 0;
}
