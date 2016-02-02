#!/bin/csh
#Write a shell script that will read the names of two directories <dir1> and <dir2> from the user, and to the following:
#a) Copy all the files with extension '*.c” in <dir1> to <dir2>. Rename the files as '1.c', '2.c', '3.c', etc. Add a comment line in the beginning of each file as:i. /** Old file name: test.c, New file name: 3.c, Modified by: username **/
#b) Compile all the newly created C programs in <dir2>, and name the executable files as '1.out', '2.out', etc.
#c) Add a line at the end of every file mentioning the date and time of modification.


echo "Enter the source directory:"
set sdir = $<
echo "Enter the destination directory:"
set ddir = $<

` cp $sdir/*.c $ddir `
set user = ` whoami`
set counter = 1
foreach file ( ` ls $ddir/*.c ` )
	echo $file
	sed -i "1i /** Old file name: $file, New file name: $counter.c, Modified by: $user  **/" $file
	mv "$file" "$ddir/$counter.c"	
	@ counter = $counter + 1
end

set counter = 1
foreach file ( ` ls $ddir/*.c ` )
	` gcc $file -o $ddir/$counter.out `
	@ counter = $counter + 1
	echo "/*Date and Time of modification: ` date ` */" >> $file
end

