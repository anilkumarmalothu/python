# creating custom threads in python
import threading 
import time
# inheriating the actual 
lock=threading.Lock()
class mythread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name

        self.counter=counter
        print("my thread is created")
    def run(self): 
       print(f"starting {self.name}\n")
    #    lock.acquire()
       print_data(self.name,5,self.counter)
    #    lock.release()
       print(f"existing {self.name}\n")
       
def print_data(threadname,delay,counter):
    count=2
    while count:
        time.sleep(delay)
        print("%s: %d" %(threadname,counter))
        count-=1    
        
thread1=mythread(100,"thread1",1)
thread2=mythread(200,"thread2",2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("program completed")

            