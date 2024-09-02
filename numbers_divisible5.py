li=[]
for i in range(6):
    x=int(input("enter the value"))
    li.append(x)
for i in range(len(li)):
    if(li[i]%5==0):
        print(li[i])    