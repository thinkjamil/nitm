Last modified: Sat Aug 29 11:36:34 IST 2015
#!/bin/csh
#Implement a rudimentary calculator using shell scripts. The script will ask the user to enter two numbers and an operator ('+', '-', '*' or '/'), perform the requested operation and print the result. The program will be running in a loop and will exit only when the user enters 'X' for the operator name.

while ( 1 )
	echo 'Enter operator'
	set op = $<
	if ( $op == 'X' || $op == 'x' ) then
		break
	endif
	echo 'Enter first operand'
	set a = $<
	echo 'Enter second operand'
	set b = $<
	set c = 0
	@ c = $a $op $b
	echo $a $op $b ' = '$c
end
