number=[2,12,23,45,35,67]

def fun(x):
    val=x  
    cnt=0  
    while val>1:
        if x%val==0:
           cnt+=1
        val-=1
    if cnt==2:
        return True
    else:
        return False       
         
val=list(filter(fun,number))
print(val)