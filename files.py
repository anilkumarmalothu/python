#  Write all content of a given file into a new file by skipping line number 5
#writing into a file 
f1=open("sample.txt","w")
f1.write("line1\n")
f1.write("line2\n")
f1.write("line3\n")
f1.write("line4\n")
f1.write("line5\n")
f1.write("line6\n")
f1.close()
#reading from file
f2=open("sample.txt")