#!/bin/csh
#Write a shell script to input 20 numbers from a file and check whether the number is prime or not. Then print the output to another file as “The number 2 is a prime number”, etc.

foreach i ( ` cat nos `)

	set flag = 0
	set ii = 0
	@ ii = $i / 2
	set j = 2
	set t = 0
	echo $ii
	while ( $j <= $ii )
		@ t = $i % $j
		if ( $t == 0 )then
			set flag = 1		
		endif
		@ j = $j + 1
	end
	if ( $flag == 1 ) then
		echo The Number $i is not a prime number >> preport
	else
		echo The Number $i is a prime number  >> preport
	endif
end

