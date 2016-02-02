#!/bin/csh
#Write a shell script that will take command line arguments as:
#./myscript <path> file1 file2 file3 .....
#and perform the following operations on the files <path>/file1, <path>/file2, etc.
#a) Replace all occurrences of the word “Calcutta” by “Kolkata”
#b) Copy the first 3 lines to the end of the file
#c) Change all alphabets on lines 6, 7 and 8 to UPPERCASE.
#d) Delete the last two lines of the filee) Insert a line after line number 5 with the text “New line inserted”
#f) Delete all lines that does not contain at least one vowel


if( $#argv < 2 )then
    echo "see usage, not enough parameters"
    exit (1)
endif
set p = $1
foreach argmnt ( $* )
	if ( $argmnt != $p) then
		set file = " $p/$argmnt"
		sed -i "s/Calcutta/Kolkata/g" $file
		head -n 3 $file >>$file
		sed -i '6,7 s/\(.*\)/\U\1/' $file
		sed -i '$ d' $file
		sed -i '$ d' $file
		sed -i '5 a New line inserted' $file
		sed -i "/[aeiou]/!d" $file
	endif
end
