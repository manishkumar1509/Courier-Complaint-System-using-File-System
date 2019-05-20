import sys,re
import os
sec_file="sec_index.txt"
txt_file="complaint.txt"
idx_file="index_file.idx"
key=sys.argv[1]

record=[]
record=open(txt_file).readlines()
secrecord=[]
secrecord=open(sec_file).readline()

def sec_search(sec_file,key):
	flag=0
	sec_f=open(sec_file,"r")
	for line in sec_f:
		list=line.split()
		if re.match(key,list[0]):
			flag=1
			val=list[1]
			search(txt_file,idx_file,val)
			break
			
			
	if(flag==0):
			print("No such record exists")
	sec_f.close()


def search(txt_file,idx_file,key):
	flag=0
	idx_f=open(idx_file,"r")
	for line in idx_f:
		if re.match(key,line):
			flag=1
			l=line.split()
			n=len(l)
			txt_f=open(txt_file,"r")
			for i in range (1,n):
				c=int(l[i])
				#print(record[c-1])
			#return l
				l2=record[c-1].split('|')
			print("\nComplaint ID:"+l2[0])
			print("Complainee's name:"+l2[1])
			print("Complaint against:"+l2[2])
			print("Complaint date:"+l2[3])
			print("Complaint timme:"+l2[4])
			print("complaint description:"+l2[5])
			print("Complaint status:"+l2[6]+"\n")
			
			txt_f.close()
			
	if(flag==0):
			print("No such record exists")
	idx_f.close()
	

sec_search(sec_file,key)
