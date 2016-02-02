#!/bin/csh
if( $#argv != 2 )then
    echo "see usage, not enough parameters"
    goto done
endif
set sdir=$1
set ddir=$2
if( ! -d $sdir )then
    echo 'souce dir not found'
    exit 1
endif
echo $sdir
echo $ddir
if(-e ddir)then 
    echo 'found destination dir'
    exit 1
endif
mkdir $ddir
foreach file ($sdir/*)
    if(-d $file)then
        echo skipping $file
    else
        echo copying $file
        cp $file $ddir
    endif
end
done: exit 
