#!/bin/csh
#Write a shell script that will take a number of command line arguments as: ./myscript num1 num2 num3 ...... num_k
# a) and compute and print the GCD of the numbers.

set flag = 0
set a = $1
set b = 1
foreach c ( $* )
	@ b = $c
	while ( $a != $b)
		if( $a > $b) then
			@ a = $a - $b
		else
			@ b = $b - $a
		endif
	end
	@ a = $b
	set flag = 1
end

echo "GCD : " $a
