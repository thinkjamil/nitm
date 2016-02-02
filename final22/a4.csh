#!/bin/csh
#Write a shell script that reads the name of a person and prints it in initial-dot form. For example, if the name entered in “Rupak Kumar Das”, it will be printed as “R. K. Das”.

if( $#argv != 3 )then
    echo "see usage, not enough parameters"
    exit (1)
endif
set fn=`echo $1|cut -c-1`
set mn=`echo $1|cut -c-1`
echo $fn. $mn. $3
