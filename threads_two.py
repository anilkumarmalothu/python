import threading

def details(name,number):
    print(f"name:{name},id:{number}")
    return 
my_threads=[]

for k in range(5):
    name=input("enter the name:")
    eid=int(input("enter the id: "))
    t=threading.Thread(target=details,args=(name,eid))
    my_threads.append(t)
    t.start()
    t.join()
for item in my_threads:
    print(item.name)    