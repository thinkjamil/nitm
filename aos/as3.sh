#!/bin/csh
echo enter file name
set fname=$<
#1
cat $fname| sed 's/monday/tuesday/'>day1
#2
cat $fname| sed 's/day/night/g'>day2
#3
cat $fname| sed 'y/ab/AB/'>day3
#4
cat $fname| sed '1,3s/day/night/'>day4
