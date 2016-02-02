Last modified: Sat Aug 29 11:36:34 IST 2015
#!/bin/csh
#Write a shell script to interactively read the marks obtained by a student in five subjects, and print the minimum, maximum and the average marks.

echo 'Enter the marks of 5 subjects'
set min = 100
set max = 0
set total = 0
set it = 1
while ( $it <= 5 )
	echo 'Enter subject '$it
	set marks = $<
	if ( $marks > $max ) then
		@ max = $marks
	endif
	if ( $marks < $min ) then
		@ min = $marks
	endif
	@ it = $it + 1
	@ total = $total + $marks
end
set avg = $total
@ avg = $avg / 5
echo 'Minimum : '$min
echo 'Maximum : '$max
echo 'Average : ' $avg

