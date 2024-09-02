# normal conditional execution 
ice_cream=["vanilla","choco bar","butter scotch","casatta"]
my_icecream=[]
for ice in ice_cream:
    if(len(ice)>8):
        my_icecream.append(ice)

print(my_icecream)        

#list comprehension


my_icecream=[ice.upper() for ice in ice_cream if len(ice)>8]
print(my_icecream)

num=[i for i in range(0,10)]
print(num)


num=[i for i in range(0,10) if (i%2)==0 ]
print(num)

num=[i**2 for i in range(0,10)]
print(num)
