#!/bin/bash

echo "Time uncertainty: "
read u_time
count=0
name="trialoutput"
fitstag=".fits"

awk -F , 'NR >= 2 && NR <= 600 { print NR " " $3 " " $4 " " $5 " " $6 " " $8 }' chime4.csv |
while read -r lineno col3 col4 col5 col6 col8
do
	if (( $(echo "$col4 > $col6" |bc) ))
	then
		max_error=$col4
	elif  (( $(echo "$col4 < $col6" |bc) ))
	then
		max_error=$col6
	else
		max_error=$col4
	fi
	count=$((count+1))
	file_name="${name}${count}${fitstag}"
	time_max=$(echo "$col8 + $u_time" | bc)
	time_min=$(echo "$col8 - $u_time" | bc)
	gtselect infile=lat_alldata_filtered.fits outfile=$file_name ra=$col3 dec=$col5 rad=$max_error evclass=128 evtype=3 tmin=$time_min tmax=$time_max emin=30 emax=1000000 zmax=180
	echo "${count} / 600"
done
