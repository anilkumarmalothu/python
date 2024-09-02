def check_list(lis):
    if(lis[0]==lis[-1]):
        return True
    else:
        return False
l=[]
for i in range(5):
    x=list(input("enter the values"))
    l.append(x)
print("it is :",check_list(l))        
    