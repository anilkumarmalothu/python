try:
    my_file=open("lambda.py","r")
    print("name of the file",my_file.name)
    print("is this file is closed ?",my_file.closed)
    print("opening mode",my_file.mode)
    print(my_file.read(20)) #read 1st 20 characters
    print(my_file.tell())#tells the current positon of file pointer
    my_file.seek(15)#file pointer shifted to 15 position 
    print(my_file.tell())
    print(my_file.readline())#reads the enter single line 
    my_file.close()
    my_file1=open("sample.txt","w")
    my_file1.write("welcome to my programming world")
    my_file1.close()
    
except FileNotFoundError as ex1:
    print(ex1)
except IOError as ex2:
    print(ex2)
except:
    print("error occured")            