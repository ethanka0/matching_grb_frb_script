import pandas as pd
import math
import time

start = time.process_time()

counter_chime = 1
counter_fermi = 0
progress = 0
def progress_bar():
	progress = (counter_chime / frbevents_num) * 100
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



grbcatalog_name = input ("Please input name of the LAT data file with the .csv tag and fulfilling the following requirements: \n ra in column 1 \n dec in column 2 \n event time in column 3 \n photon label in column 4\n")
fermievents_num = input ("Please input the number of entries in the LAT data file: ")
fermievents_num = int(fermievents_num)
fermievents_num = fermievents_num - 1
frbcatalog_name = input ("Please input name of the CHIME catalog with the .csv tag and fulfilling the following requirements: \n frb code under column named 'tns_name' \n ra under column named 'ra' \n dec under column named 'dec' \n ra uncertainty under column named 'ra_err' \n dec uncertainty under column named 'dec_err' \n event observed time under column named 'time'")
frbevents_num = input ("Please input number of entries in the CHIME catalog: ")
frbevents_num = int(frbevents_num)
frbevents_num = frbevents_num - 1
u_time = input ("Please input uncertainty of time in seconds i.e. ['3600' for an hour], ['86400' for a day]:  ")

u_time = str(u_time)
name_file1 = "matchingloc_" + u_time + "s.txt"
name_file2 = "matchingloc_and_time_" + u_time + "s.txt"
u_time = float(u_time)

frbcatalog = pd.read_csv(frbcatalog_name) #CHIME data file
grbcatalog = pd.read_csv(grbcatalog_name) #LAT data file
f=open(name_file1, "w") #File that only lists events matching origin
g=open(name_file2, "w") #File that only lists events matching origin and time


while counter_chime < frbevents_num : # of rows of chime data
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
	while counter_fermi < fermievents_num: # of rows of FERMI data
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
				frb_overlap_time_loc.append(frbcode)
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
