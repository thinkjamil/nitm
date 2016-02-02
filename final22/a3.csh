#!/bin/csh
#Write a shell script to perform the following operations on all files with extension '.txt' in the currect directory and all its subdirectories:
#a) Insert the following line in the beginning of every file: “Last modified: <today's date>”
#b) Rename the file by changing the extension from '.txt' to '.text.
#c) Count the number of words in every file that contains at least two vowels, and print a report

foreach file  ( ` find -name '*.txt' -type f ` )
	echo $file
	set dt = `date`
	sed -i '1i\'"Last modified: $dt" $file
	rename 's/\.txt$/\.text/' $file
end
foreach file ( ` find -name '*.text' -type f `)
	set wcount = 0
	foreach word (` cat $file ` )
		if ( `echo $word | tr -cd 'aeiou' | wc -c` >= 2 ) then
			@ wcount = $wcount + 1
		endif
	end	
	echo $wcount $file
end

