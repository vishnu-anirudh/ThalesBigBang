#!/usr/bin/python

import sys

class FileClone:
	def __init__(self):
		nothing=1

	def main(self, inp_name, max_dist, inp_lsensor, inp_lwheel1, inp_lwheel2,inp_rsensor, inp_rwheel1, inp_rwheel2):

		#########################
		#Input
		#inp_name - name of user
		#max_dist=maximum distance
		#inp_lsensor - (ON)/(OFF)
		#inp_lwheel1 (if lsensor is ON) - FORWARD/BACKWARD
		#inp_lwheel2 (if lsensor is OFF)- FORWARD/BACKWARD

		#inp_rsensor - (ON)/(OFF)
		#inp_rwheel1 (if rsensor is ON) - FORWARD/BACKWARD
		#inp_rwheel2 (if rsensor is OFF)- FORWARD/BACKWARD
		
		#########################

		#User's input shall be taken from GUI
		#
		file_path='arduino_files/'
		user_name=inp_name
		target=open(file_path+user_name+'.ino', 'w')

		#Open the file which has the code frame
		#
		f=open('kids_gui/sample.txt')

		#Preprocessing
		#
		#Left sensor 
		#
		if(inp_lsensor=="(ON)"):
			lsensor=True
		else:
			lsensor=False

		#Left wheel (left sensor if ON)
		#
		if(inp_lwheel1)=="FORWARD":
			#inp_lwheel1=FORWARD and inp_lsensor=(ON)
			lwheel_sensor_on=200
		else:
			#inp_lwheel1=BACKWARD and inp_lsensor=(ON)
			lwheel_sensor_on=800

		#Left wheel (left sensor if OFF)
		#
		if(inp_lwheel2)=="FORWARD":
			#inp_lwheel2=FORWARD and inp_lsensor=(OFF)
			lwheel_sensor_off=200
		else:
			#inp_lwheel2=BACKWARD and inp_lsensor=(OFF)
			lwheel_sensor_off=800


		#Right sensor
		#
		if(inp_rsensor=="(ON)"):
			rsensor=True
		else:
			rsensor=False

		#Right wheel (Right sensor if ON)
		#
		if(inp_lwheel1)=="FORWARD":
			#inp_rwheel1=FORWARD and inp_rsensor=(ON)
			rwheel_sensor_on=800
		else:
			#inp_rwheel1=BACKWARD and inp_rsensor=(ON)
			rwheel_sensor_on=200

		#Right wheel (right sensor if OFF)
		#
		if(inp_lwheel2)=="FORWARD":
			#inp_rwheel2=FORWARD and inp_rsensor=(OFF)
			rwheel_sensor_off=800
		else:
			#inp_rwheel2=BACKWARD and inp_rsensor=(OFF)
			rwheel_sensor_off=200


		#Input from GUI
		#
		inp_2=lwheel_sensor_on
		inp_1=lwheel_sensor_off
		inp_4=rwheel_sensor_on
		inp_3=rwheel_sensor_off
		inp_5=max_dist


		lines=f.readlines()

		for line in lines:
			#print line

			#i=input("write something")

			if 'Input1' in line:
				line1=line[0:(len(line)-len('Input1')-2)]+str(inp_1)+';'
				target.write(line1)
				target.write('\n')
				#print line1


			elif 'Input2' in line:
				line1=line[0:(len(line)-len('Input2')-2)]+str(inp_2)+';'
				target.write(line1)
				target.write('\n')

			elif 'Input3' in line:
				line1=line[0:(len(line)-len('Input3')-2)]+str(inp_3)+';'
				target.write(line1)
				target.write('\n')
            
			elif 'Input4' in line:
				line1=line[0:(len(line)-len('Input4')-2)]+str(inp_4)+';'
				target.write(line1)
				target.write('\n')

			elif 'Input5' in line:
				line1=line[0:(len(line)-len('Input5')-2)]+str(inp_5)+';'
				target.write(line1)
				target.write('\n')

			elif '    if (L_distance > 0)//[change_here]' in line:
				if not lsensor:
					line1='    if (L_distance == 0) '
					target.write(line1)
					target.write('\n')

				else:
					target.write(line)

			elif '    if (R_distance > 0)//[change_here]' in line:
				if not rsensor:
					line1='    if (R_distance == 0) '
					target.write(line1)
					target.write('\n')

				else:
					target.write(line)
			else:
				target.write(line)
				#print line

		f.close()
		target.close()


#app = FileClone()
#app.main(sys.argv[1],sys.argv[2],sys.argv[3], sys.argv[4])
