string=input("enter the initial string")


for l in range(10):
    bulls=0
    cows=0
    print(f"enter {l+1} choice: ")
    if(bulls!=len(string)):
        string1=input("enter the string to play----")
    if(bulls==len(string)):
        break
    
    for i in range(len(string)):
    
        if(string1[i]==string[i]):
            bulls+=1
        elif string1[i] in string:
            cows+=1 
    print(f"the number bulls are {bulls}")  
    print(f"the number cows are {cows}")        
if(bulls==len(string)):        
    print(".....you won.....")
else:           
    print(f"the number bulls are {bulls}")  
    print(f"the number cows are {cows}")      
            