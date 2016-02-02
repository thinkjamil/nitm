#!/bin/csh
#Create two directory Input and Output. Write a c code that reads a file and copy the content to another file.
#a) Write a shell script which will do this for 20 files.
#b) Must read the files from Input directory and output the file to Output directory
set counter = 0
echo 'Enter input file path'
set inputd = $<
echo 'Enter output file path'
set outputd = $<
foreach file ( `ls $inputd` )
	@ counter = $counter + 1
	if ( $counter > 20 ) then 
		break
	endif
	set inputf = "$inputd/$file"
	set outputf = "$outputd/$file"
	`./filecopy $inputf $outputf`
end
