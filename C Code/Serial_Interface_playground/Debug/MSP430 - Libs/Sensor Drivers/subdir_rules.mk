################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Each subdirectory must supply rules for building sources it contributes
MSP430\ -\ Libs/Sensor\ Drivers/MS5837-30BA.obj: ../MSP430\ -\ Libs/Sensor\ Drivers/MS5837-30BA.c $(GEN_OPTS) | $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: MSP430 Compiler'
	"" -vmspx --data_model=restricted --use_hw_mpy=F5 --include_path="/msp430/include" --include_path="/include" --advice:power=all -g --define=__MSP430F5529__ --diag_warning=225 --diag_wrap=off --display_error_number --silicon_errata=CPU21 --silicon_errata=CPU22 --silicon_errata=CPU23 --silicon_errata=CPU40 --printf_support=minimal --preproc_with_compile --preproc_dependency="MSP430 - Libs/Sensor Drivers/MS5837-30BA.d" --obj_directory="MSP430 - Libs/Sensor Drivers" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

MSP430\ -\ Libs/Sensor\ Drivers/Razer_AHRS.obj: ../MSP430\ -\ Libs/Sensor\ Drivers/Razer_AHRS.c $(GEN_OPTS) | $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: MSP430 Compiler'
	"" -vmspx --data_model=restricted --use_hw_mpy=F5 --include_path="/msp430/include" --include_path="/include" --advice:power=all -g --define=__MSP430F5529__ --diag_warning=225 --diag_wrap=off --display_error_number --silicon_errata=CPU21 --silicon_errata=CPU22 --silicon_errata=CPU23 --silicon_errata=CPU40 --printf_support=minimal --preproc_with_compile --preproc_dependency="MSP430 - Libs/Sensor Drivers/Razer_AHRS.d" --obj_directory="MSP430 - Libs/Sensor Drivers" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

