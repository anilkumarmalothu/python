import threading


def print_hello():
    count=10
    while(count>0):
        print("hello")
        count-=1
def print_hi(name):
    print(f"hi {name} !!!")
    
try:
    t1=threading.Thread(target=print_hello,name="thread1")
    t1.start()
    t1.join()
    t2=threading.Thread(target=print_hi,args=("anil",))
    t2.start()
    # t2.join()
except:
    print("error: unable to start thread")
print(threading.current_thread().name)                    