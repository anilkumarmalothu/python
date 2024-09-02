
def fun(name):
 print(len(name))
 if 'sampath' in name: 
  name.sort()
 
 return name
names=['sony','anil','mani','kalyan']
names.insert(2,"sampath")
print(names)
print(fun(names)) 
    
