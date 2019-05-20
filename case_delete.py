import re
import sys

def index_text_file(txt_filename, idx_filename, 
    delimiter_chars=",.;:!?"):
        txt_fil = open(txt_filename, "r")
        """
        Dictionary to hold words and the line numbers on which 
        they occur. Each key in the dictionary is a word and the 
        value corresponding to that key is a list of line numbers 
        on which that word occurs in txt_filename.
        """

        word_occurrences = {}
        line_num = 0

        for lin in txt_fil:
            line_num += 1
            words=re.findall('C...',lin)
            words2 = [ word.strip(delimiter_chars) for word in words ]
            # Find and save the occurrences of each word in the line.
            for word in words2:
                if word in word_occurrences:
                    word_occurrences[word].append(line_num)
                else:
                    word_occurrences[word] = [ line_num ]


        if line_num < 1:
            print("No lines found in text file, no index file created.")
            txt_fil.close()
            sys.exit(0)

        # Display results.
        word_keys = word_occurrences.keys()
        #print "{} unique words found.".format(len(word_keys))
        word_keys = word_occurrences.keys()

        # Sort the words in the word_keys list.
        sorted(word_keys)

        # Create the index file.
        idx_fil = open(idx_filename, "w")

        for word in word_keys:
            line_nums = word_occurrences[word]
            idx_fil.write(word + " ")
            for line_num in line_nums:
                idx_fil.write(str(line_num) + " ")
            idx_fil.write("\n")

        txt_fil.close()
        idx_fil.close()

record=[]
record=open("complaint.txt").readlines()


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
                                l2=record[c-1].split('|')
                        print("\nComplaint ID:"+l2[0])
                        print("Complainee's name:"+l2[1])
                        print("Complaint against:"+l2[2])
                        print("Complaint date:"+l2[3])
                        print("Complaint time:"+l2[4])
                        print("Complaint description:"+l2[5])
                        print("Complaint status:"+l2[6]+"\n")
                        txt_f.close()
                        n=len(l)
                        l2=[]
                        for i in range(1,n):
                                l2.append(int(l[i]))

                        file1=open("complaint.txt","w")
                        n=len(record)
                        record2=[]
                        for i in range(1,n+1):  #line number in the original file(1 to ...)
                                if i not in l2:
                                        record2.append(record[i-1])
                        print("Record deleted.\n")
                        file1.writelines(record2)
                        file1.close()
                        index_text_file("complaint.txt","index_file.idx")

        if(flag==0):
                print("No such record exists")
        idx_f.close()

search("complaint.txt","index_file.idx",sys.argv[1])
