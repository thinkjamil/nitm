#!/bin/csh

echo Enter ur name
set name=$<
echo $name
set date_field=`date`
echo $date_field[1]
foreach field(`date`)
	echo $field
end
