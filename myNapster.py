#!/usr/bin/env python3


#IMPORT LIBRARIES
import speech_recognition as sr
import os


#CREATING SYNONYMS DICTIONARY
mk=['make','create','mk']		#DO THE INSERTIONS IN THE BEG. (CREATE SYNO.)
rm=['delete','remove','drop','rm']	#DO THE INSERTIONS IN THE BEG. (REMOVE SYNO.)
dictionary_op=[mk,rm]			#TO DETECT OPERATION

dir_type=['directory','folder','folders','dir']
file_type=['file','files','fi']
dictionary_type=[dir_type,file_type]	#TO DETECT OPERATION TYPE

count=['total','number','num']
dictionary_count=[count]

#RECOGNIZER DEFINED
r=sr.Recognizer()


	## CREATING FUNCTIONS ## ------------------------------------------------------------------------------------------------

#ASKS FOR THE FILE/FOLDER NAME IF REQUIRED ( --RETURNS NAME OF FILE-- )
def ask_name():
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print("Can you mention the name?")
		audio=r.listen(source)
	try:
		name=r.recognize_google(audio)
		return name
	except:
		print("Sorry, could Not Understand!!")
		pass



#ASKS FOR THE LOCATION IF REQUIRED ( --RETURNS LOC. OF FILE-- )
def ask_path():
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print("Can you mention the path or location ?")
		audio=r.listen(source)
	try:
		raw_path=r.recognize_google(audio)
		strip_data=raw_path.strip()
		split_data=strip_data.split()
		print(split_data)
	
		## THINK FOR THE SOLUTION ##

	except:
		print("Sorry, could Not Understand!!")
		pass


#CONVERTING LIST TO LOWER CASE ( --RETURNS LIST AS ARGUMENT INTO LOWER CASE-- )
def tolower(ip_list):
	for i in range(0,len(ip_list)):
		ip_list[i]=ip_list[i].lower()
	return ip_list


#DICTIONARY CHECKING FOR REQUIRED DETAILS ( --RETURNS MULTIPLE-- ) 

def check_dict(ip):
	operation='null'
	op_type='null'
	count_type='null'
	#TO DETECT OPERATION TO PERFORM
	for i in range(0,len(ip)):
		for j in range(0,len(dictionary_op)):
			if ip[i] in dictionary_op[j]:
				operation = dictionary_op[j][-1]
				break
			
	#TO DETECT FILE TYPE ON WHICH OPERATION WILL BE PERFORMED		
	for p in range(0,len(ip)):
		for k in range(0,len(dictionary_type)):
			if ip[p] in dictionary_type[k]:
				op_type = dictionary_type[k][-1]
				break
			
	#TO DETECT WEATHER TO COMPUTE TOTAL FILES OR TOTAL FOLDER PRESENT IN DIR		
	for p in range(0,len(ip)):
		for k in range(0,len(dictionary_count)):
			if ip[p] in dictionary_count[k]:
				count_type = dictionary_count[k][-1]
				break

	return operation ,op_type,count_type
	#return ("\nI have been designed to perform directory operations, not to handle your BULLSHIT!!!")


#CREATING FOLDER ( --RETURNS NOTHING-- )
def create_dir():
	dir_name=ask_name()
	os.system('mkdir '+dir_name)

#REMOVING FOLDER ( --RETURNS NOTHING-- )	## NEED TO EMPTY THE FOLDER BEFOREHAND (INTEGRATE EMPTY_DIRECTORY FUNCTION AFTER DONE)
def remove_dir():
	dir_name=ask_name()
	os.system('rmdir '+dir_name)
	
#RENAMING FOLDER ( --RETURNS NOTHING-- )
def rename_dir():
	source_dir=ask_name()
	new_dir=ask_name()
	os.system('mv '+source_dir+' '+new_dir)

#COUNT DIRECTORIES AND FILES ( ** 2 functions **) ( --RETURNS NOTHING-- )
#DIRECTORY
def count_dir():
	total_dirs=0
	for root,dirs,files in os.walk('/home/priyank/Desktop/',topdown=True):
		for all in range(0,len(dirs)):
			total_dirs = total_dirs + len(dirs[all])
	print('Total directories present on Desktop: ',total_dirs)
#FILES
def count_file():
	total_files=0
	for root,dirs,files in os.walk('/home/priyank/Desktop/',topdown=True):
		for all in range(0,len(files)):
			total_files = total_files + len(files[all])
	print('Total files present on Desktop: ',total_files)




 	## MAIN PART ## -----------------------------------------------------------------------------------------------------------------


#INITIAL INTRACTION WITH USER
with sr.Microphone() as  source:
	r.adjust_for_ambient_noise(source)
	print ("Heyyy, Whatsup chief!!!")
	print("How can i help you?")	
	audio=r.listen(source)

try:
	
	speech_ip=r.recognize_google(audio)	#speech_ip --> VOICE INPUT
	print(speech_ip)
	
	#VOICE DATA CLEANING
	stripped_data=speech_ip.strip()		#____Removing extra spaces
	data=stripped_data.split()		#____Fetching individual words spoken
	data=tolower(data)
	print(data)
	
	#DICTIONARY CHECKING FOR KEYWORDS
	operation,op_type,count_type=check_dict(data)
	#print(operation)	
	#print(op_type)
	#print(count_type)
	
	if operation=='mk' and op_type=='dir':
		create_dir()
	elif operation=='rm' and op_type=='dir':
		remove_dir()
	elif ('rename' in data) and op_type=='dir':
		rename_dir()
	elif count_type=='num' and operation == 'null' :
		if op_type=='dir':
			## folder
			count_dir()
		elif op_type=='fi':
			## files
			count_file()
		else :
			## files+folder
			count_dir()
			count_file()

	else :
		#print("I have been designed to perform directory operations, not to handle your BULLSHIT!!!")
		print("\nSeriously, what do you think i am? A Freakin GOD.")
		print("\nI am KIRA, get that stuck in your head.\n")
	
except:
	print("Could Not Understand!!")
	pass



