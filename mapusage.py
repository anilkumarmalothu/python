def fun(x):
    if x=="sreeram":
     return x +" "+ "s"
    if x=="anil":
        return x +" m"
    if x=="hello":
        return x +" "
a = {2:"sreeram",3:"anil",4:"hello"}
val=map(fun,a.values())
b = dict(zip(a.keys(),val))
print(b)  
    