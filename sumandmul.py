def sum(list1):
    val=0
    for i in range(len(list1)):
        val+=list1[i]
    return val    
def multiply(list2):
    mul=1
    for i in range(len(list2)):
        mul*=list2[i]
    return mul
list3=[1,2,3,4,5]
val1=sum(list3)
val2=multiply(list3)    
print(f"the sum of list is {val1}")
print(f"the multiplication list is {val2}")    
        