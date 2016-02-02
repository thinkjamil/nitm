#!/bin/csh
if( $#argv != 1 )then
    echo "see usage, not enough parameters"
    goto done
endif
set no=$1

if( $no <= 100 )then
	echo "Number $no in range of [0,100]"
else if( $no <= 200)then
	echo "Number $no in range of [101,200]"
else
	echo "Number $no in range of [201,infinity]"
endif

