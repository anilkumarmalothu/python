data=[]

for i in range(10):
    ele=int(input("enter the number"))
    data.append(ele)
print(data)   

total=sum(data,10)
print("total: ")
print(total)
data.sort()
print("minimum number in list is")
print(data[0])
print("largest number in list :")
print(data[-1])
print("average:")
print(total/len(data))