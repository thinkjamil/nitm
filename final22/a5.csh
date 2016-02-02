#!/bin/csh
#Write a shell script that reads all the files in a specified directory, and print the following:
#a) File name and size (in number of bytes)
#b) Type of the file (regular, directory or special)
#c) Access permissions (read-only, write-only, executable, etc.)
#d) Number of lines, and words in every file

if ($#argv != 1) then
        echo "Usage: $0 dir1 dir2"
endif
set dir1=$1
if (! -d $dir1) then
	echo "$dir1 is not a directory" ; exit 1
endif
foreach file ($dir1/*)
	echo name - `stat -c %n $file`
	echo  file type - `stat -c %F $file`
	echo access rights - `stat -c %A $file`
	echo size - `stat -c %s $file`
	echo lines - `wc -l $file`
	echo words - `wc -w $file`
end
