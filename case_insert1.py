import sys
import re
import os

case_desc1=""
txt_filename="complaint.txt"
txt_fil = open(txt_filename, "a")
txt1 = open("complaint.txt","r")
txt_indexname="index_file.idx"
n=len(sys.argv)
C_ID=sys.argv[1]
C_name=sys.argv[2]
C_against=sys.argv[3]
C_date=sys.argv[4]
C_time=sys.argv[5]

C_status=sys.argv[6]
flag=0
for x in txt1:
    if(C_ID in x):
        flag=1
if flag==0:
    for i in range(7,n):
        C_desc=case_desc1+sys.argv[i]+" "
    entry=C_ID+' '+'|'+C_name+'|'+C_against+'|'+C_date+'|'+C_time+'|'+C_desc+'|'+C_status+'|'+'\n'
    txt_fil.write(entry)
else:
    print("Already exists")
txt_fil.close()

def index_text_file():

    d={}
    d1={}  
    comp_file = open("complaint.txt","r")
    idx_file_r = open("index_file.idx","r")
    l=0
    for line in comp_file:
        l=l+1
    for x in idx_file_r:
        list = x.split()
        d1 = {list[0]:list[1]}
        d.update(d1)
    d1={C_ID:l}
    d.update(d1)
    idx_file_w = open("index_file.idx","w")
    for i in sorted(d):
        #data = 
        idx_file_w.write(i+" "+str(d[i])+"\n")
    print(d)
    comp_file.close()
    comp_file = open("complaint.txt","r")
    sec_file=open("sec_index.txt","w")
    secd={}
    secd2={}
    for line in comp_file:
    	list=line.split("|")
    	secd2={list[1]:list[0]}
    	secd.update(secd2)
    for i in sorted(secd):
    	sec_file.write(i+" "+str(secd[i])+"\n") 
    print(secd)

index_text_file()
    
