
string=input("enter the string ")
res=""
for i in range(len(string)):
    if string[i] in "AEIOU":
      res+=string[i].lower()
    else:
        res+=string[i]
print(res)             
        
            
        