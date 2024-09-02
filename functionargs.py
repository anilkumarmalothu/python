def skill_set(name,*skills):  #*args ,allows zero or more values
    print("printing the skills",name)
    for skill in range(len(skills)):
        print(skills[skill])
skill_set("anil","c","c++","python")  
skill_set("sreeram")


def skills(name="hello",**args): #kargs(keyword arguments)
    print("printing skill set of ",name)
    for i in args:
        print(i,args[i])
    
        
skills("shobidh",skill_1="c",skill_2="c++")
skills()        
