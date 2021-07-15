# matching_grb_frb_script

## matching_frbgrb_finder_python.py ##
This python script can be used to find overlapping events between 2 catalogs. It compares the location (RA/DEC) and time of event to find any similarities.
It is used in step 2 of my analysis into the "Search for Gamma-ray Emissions from a Population of Fast Radio Bursts."

Usage requirements:
- The script requires .csv files and knowledge of what column contains the GRB/FRB code, the event time, RA, DEC, and RA/DEC errors.
- Input a time uncertainty when prompted, filenames, and number of entries in each file
- The script displays when a match is found and it will output a total runtime at the end as well as the time the script finished
- The package 'pandas' is required which can be installed here: https://pandas.pydata.org/getting_started.html
- Generates 2 .txt files, one containing photons and FRBs that only match in location and the other containing photons and FRBs that mathc in both location and time.



## matching_frbgrb_finder_bash.sh ##
This bash script utilises the Fermi tool 'gtselect' and is much more optimised than the python version above. It is used in step 2 of my analysis into the "Search for Gamma-ray Emissions from a Population of Fast Radio Bursts."

Usage requirements:
- Have Fermi tools pre installed and he conda enviornment activated (https://github.com/fermi-lat/Fermitools-conda/wiki/Installation-Instructions)
- Activate Fermi enviornment
- Input a time uncertainty and energy range when prompted
- Requires the data and knowledge of what column contains the GRB/FRB code, the event time, RA, DEC, and RA/DEC errors.
- The script can be adapted by changing the lines with comments. 


These scripts was produced by Ethan H. Kao at the Laboratory for Space Research (HKU)

For any questions, contact: ethankao0910@gmail.com
