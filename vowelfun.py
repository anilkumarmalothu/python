def is_vowel(char1):
    if(char1=="a" or char1=="e" or char1=="i" or char1=="o" or char1=="u"):
        return True
    elif(char1=="A" or char1=="E" or char1=="I" or char1=="O" or char1=="U"):
        return True
    else:
        return False
string=input("enter the char ")
c=string[0]
boolean1=is_vowel(c)
if(boolean1):
    print(boolean1)
else:
    print(boolean1)    