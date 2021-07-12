#Produced by Ethan H. Kao

import pandas as pd
import math
import time

start = time.process_time()

counter_chime = 500
counter_fermi = 0
progress = 0
def progress_bar():
	progress = (counter_chime / 599) * 100
	progress = str(progress)
	print ("Progress: " + progress + "%")

frbcode = ""
chime_cra = 0
chime_cdec = 0
chime_cra_err = 0
chime_cdec_err = 0

grbcode = ""
fermi_cra = 0
fermi_cdec = 0

dis = 0
timedif = 0

grb_overlap_loc = []
frb_overlap_loc = []
grb_overlap_time_loc = []
frb_overlap_time_loc = []

frbcatalog = pd.read_csv('chime4.csv') #CHIME data file
grbcatalog = pd.read_csv('lat_alldata_loc_time.csv') #LAT data file
f=open("matchingloc2.txt", "w") #File that only lists events matching origin
g=open("matchingloc_and_time2.txt", "w") #File that only lists events matching origin and time



print ("This script uses CHIME's 1st catalog and Fermi data to find FRBs and GRBs that could originate from the same place.")
print (" This script can be adapted and modified for any .csv or .txt file by changing the lines with comments.")
u_time = input ("Please input uncertainty of time in seconds i.e. ['3600' for an hour], ['86400' for a day]:  ")
u_time = float(u_time)

while counter_chime < 599: # of rows of chime data; change the title of the columns
	progress_bar()
	counter_fermi = 0
	frbcode = frbcatalog.at[counter_chime, 'tns_name']
	chime_cra = frbcatalog.at[counter_chime, 'ra']
	chime_cdec = frbcatalog.at[counter_chime, 'dec']
	chime_cra_err = frbcatalog.at[counter_chime, 'ra_err']
	chhime_cdec_err = frbcatalog.at[counter_chime, 'dec_err']
	chime_ctime = frbcatalog.at[counter_chime, 'time']
	chime_cra = float(chime_cra)
	chime_cdec = float(chime_cdec)
	chime_ctime = float(chime_ctime)
	counter_chime +=1
	while counter_fermi < 43236723: # of rows of FERMI data; .iat can be used if table lacks a column name
		grbcode = grbcatalog.iat[counter_fermi, 3]
		fermi_cra = grbcatalog.iat[counter_fermi, 0]
		fermi_cdec = grbcatalog.iat[counter_fermi, 1]
		fermi_ctime = grbcatalog.iat[counter_fermi, 2]
		fermi_cra = float(fermi_cra)
		fermi_cdec = float(fermi_cdec)
		fermi_ctime = float(fermi_ctime)
		dis = math.sqrt(math.pow((chime_cra - fermi_cra), 2) + math.pow((chime_cdec - fermi_cdec), 2))
		if dis <= chime_cra_err or dis <= chime_cdec_err:
			print ("LOCATION MATCH FOUND")
			f.write("\n" + str(frbcode) + " matches with " + str(grbcode))
			grb_overlap_loc.append(grbcode)
			frb_overlap_loc.append(frbcode)
			timedif = abs(chime_ctime - fermi_ctime)
			if timedif <= u_time:
				g.write("\n"+ str(frbcode) + " matches in time and space with " + str(grbcode))
				grb_overlap_time_loc.append(grbcode)
				grb_overlap_time_loc.append(frbcode)
				counter_fermi +=1
				print ("----------MATCH FOUND----------")
				print (str(frbcode) + " matches in time and space with " + str(grbcode))
			else:
				counter_fermi +=1
		else:
			counter_fermi +=1
	progress_bar()

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print (current_time)
print ("^^ Completion time ^^")
print (time.process_time() - start)
print ("^^ Process time ^^")
print (frb_overlap_time_loc)
print (grb_overlap_time_loc)
