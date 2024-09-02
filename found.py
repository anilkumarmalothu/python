s=input("eneter the string:")
c=input("enetr the character to find in string:")
for i in range(len(s)):
    if(s[i]==c):
        print(f"charecter {c} is present in string at index {i}")
else:
    print(f"character found successfully")    
     