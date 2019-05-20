from tkinter import *
import os
import subprocess

#Function
def display_frame(frame) :
	frame.pack_forget()
	frame.pack()

def back() :
	global root
	global add_frame
	global frame,search_frame,delete_frame,modify_frame,add_patient_frame
	global add_case_frame,search_frame,search_patient_frame,delete_frame,delete_patient_frame,modify_frame,modify_patient_frame
	
	for i in (frame,add_frame,search_frame,delete_frame,modify_frame,add_patient_frame,search_frame,search_patient_frame,delete_frame,delete_patient_frame,modify_frame,modify_patient_frame):
	
		i.pack_forget()
	display_frame(frame)

def add() :
	global frame,root,add_frame
	frame.pack_forget()
	add_frame = Frame(root)
	button = ['Add Complaint Details','Go to Main Menu']
	function  = [add_patient,back]
	for i in range(len(button)) :
		Button(add_frame,text=button[i],command=function[i],height=1,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(add_frame)

def search() :
	global frame,root,search_frame
	frame.pack_forget()
	search_frame = Frame(root)
	button = ['Search by Complaint ID','Search by Name','Go to Main Menu']
	function  = [search_patient,search_by_name,back]
	for i in range(len(button)) :
		Button(search_frame,text=button[i],command=function[i],height=1,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(search_frame)

def delete() :
	#global add_frame
	global frame,root,delete_frame
	frame.pack_forget()
	delete_frame = Frame(root)
	button = ['Delete Complaint Details','Go to Main Menu']
	function  = [delete_patient,back]
	for i in range(len(button)) :
		Button(delete_frame,text=button[i],command=function[i],height=1,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(delete_frame)

def modify() :
	global frame,root,modify_frame
	frame.pack_forget()
	modify_frame = Frame(root)
	button = ['Modify Complaint Details','Go to Main Menu']
	function  = [modify_patient,back]
	for i in range(len(button)) :
		Button(modify_frame,text=button[i],command=function[i],height=1,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(modify_frame)


#Add Menu
def add_patient() :
	global add_frame,root,add_patient_frame
	global v1,v2,v3,v4,v5,v6,v7
	add_frame.pack_forget()
	add_patient_frame = Frame(root)
	label1=Label(add_patient_frame,text="Enter the Complaint ID.")
	label1.pack()
	v1=Entry(add_patient_frame)
	v1.pack()

	label2=Label(add_patient_frame,text="Enter the Complainee's Name.")
	label2.pack()
	v2=Entry(add_patient_frame)
	v2.pack()

	label3=Label(add_patient_frame,text="Complaint against")
	label3.pack()
	v3=Entry(add_patient_frame)
	v3.pack()

	label4=Label(add_patient_frame,text="Complaint date")
	label4.pack()
	v4=Entry(add_patient_frame)
	v4.pack()
	
	label5=Label(add_patient_frame,text="Complaint time")
	label5.pack()
	v5=Entry(add_patient_frame)
	v5.pack()

	label6=Label(add_patient_frame,text="Enter the Complaint description")
	label6.pack()
	v7=Entry(add_patient_frame)
	v7.pack()

	label7=Label(add_patient_frame,text="Enter the Complaint status")
	label7.pack()
	v6=Entry(add_patient_frame)
	v6.pack()

	b1=Button(add_patient_frame,text="Enter",command=gett)
	b1.pack(side = LEFT)
	
	b2=Button(add_patient_frame,text="Back",command=back)
	b2.pack(side = RIGHT)
	display_frame(add_patient_frame)


def gett():
	
	command='case_insert1.py '+v1.get()+" "+v2.get()+" "+v3.get()+" "+v4.get()+" "+v5.get()+" "+v6.get()+" "+v7.get()
	os.system(command)
	print(command)



#Search
def search_patient() :
	global search_frame,root,search_patient_frame
	global vs1,vs2,vs3,vs4
	global lbl
	search_frame.pack_forget()
	search_patient_frame = Frame(root)
	global vs1,vs2,vs3
	
	lbl = Label(search_patient_frame, text='')
	lbl.pack()	

	
	key=Label(search_patient_frame,text="Enter Complaint ID.")
	key.pack()
	vs3=Entry(search_patient_frame)
	vs3.pack()

	b1=Button(search_patient_frame,text="Enter",command=get1)
	b1.pack(side=LEFT)

	b2=Button(search_patient_frame,text="Back",command=back)
	b2.pack(side = RIGHT)
	display_frame(search_patient_frame)


#search by name
def search_by_name():
	global search_frame,root,search_patient_frame
	global vk1,vk2,vk3,vk4
	global lbl
	search_frame.pack_forget()
	search_patient_frame = Frame(root)
	global vk1,vk2,vk3
	
	lbl = Label(search_patient_frame, text='')
	lbl.pack()	

	
	key=Label(search_patient_frame,text="Enter Complainee's Name")
	key.pack()
	vk3=Entry(search_patient_frame)
	vk3.pack()

	b1=Button(search_patient_frame,text="Enter",command=get2)
	b1.pack(side=LEFT)

	b2=Button(search_patient_frame,text="Back",command=back)
	b2.pack(side = RIGHT)
	display_frame(search_patient_frame)



def get1():
	
	command='case_search.py '+" "+vs3.get()
	
	
	
	output = subprocess.check_output(command, shell=True)

	lbl['text'] = output.strip()
	

	os.system(command)
	print(command)

	
def get2():
	command='case_search_sec.py '+" "+vk3.get()
	output = subprocess.check_output(command, shell=True)
	lbl['text'] = output.strip()
	os.system(command)
	print(command)



#Delete
def delete_patient() :
	#global add_frame
	global delete_frame,root,delete_patient_frame
	global vd1,vd2,vd3
	global lbl1
	delete_frame.pack_forget()
	delete_patient_frame = Frame(root)
#	global vs1,vs2,vs3
	global lbl
	lbl1 = Label(delete_patient_frame, text='')
	lbl1.pack()	

	

	key=Label(delete_patient_frame,text="Enter Complaint ID.")
	key.pack()
	vd3=Entry(delete_patient_frame)
	vd3.pack()	
	
	b1=Button(delete_patient_frame,text="Enter",command=delete1)
	b1.pack(side=LEFT)

	b2=Button(delete_patient_frame,text="Back",command=back)
	b2.pack(side = RIGHT)
	display_frame(delete_patient_frame)

def delete1():
	command='case_delete.py '+" "+vd3.get()
	

	
	output = subprocess.check_output(command, shell=True)

	lbl1['text'] = output.strip()

	os.system(command)
	print(command)
	display_frame(delete_patient_frame)



#Modify
def modify_patient() :
	global modify_frame,root,modify_patient_frame
	global v1,v2,v3,v4,v5,vs4
	global lbl1
	modify_frame.pack_forget()
	modify_patient_frame = Frame(root)
	lbl1 = Label(modify_patient_frame, text='')
	lbl1.pack()
	label3=Label(modify_patient_frame,text="Enter Complaint ID.")
	label3.pack()
	v3=Entry(modify_patient_frame)
	v3.pack()
	key1=Label(modify_patient_frame,text="Enter new status")
	key1.pack()
	vs4=Entry(modify_patient_frame)
	vs4.pack()
	b1=Button(modify_patient_frame,text="Enter",command=get_modify)
	b1.pack(side = LEFT)
	b2=Button(modify_patient_frame,text="Back",command=back)
	b2.pack(side = RIGHT)
	display_frame(modify_patient_frame)

def get_modify():
	command='case_modify1.py '+" "+v3.get()+" "+vs4.get()
	print("modified")
	output = subprocess.check_output(command, shell=True)
	lbl1['text'] = output.strip()
	os.system(command)
	print(command)
	display_frame(modify_patient_frame)



#Main Program
root = Tk(className = "GUI")
frame=add_frame=search_frame=delete_frame=modify_frame = Frame(root, bg='blue')
root.minsize(200,200)
root.geometry("600x500")
root.title("Courier Complaint System")

add_patient_frame = add_case_frame = Frame(root)
search_patient_frame  = Frame(root)
delete_patient_frame  = Frame(root)
modify_patient_frame = Frame(root)


#Creating Main_Menu Frame
button = ['Add','Search','Delete','Modify']
function = [add,search,delete,modify]
for i in range(len(button)) :
	Button(frame,text=button[i],command=function[i],height=1,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
#Display
display_frame(frame)
root.mainloop()

