# creating custom threads in python
import threading 
import time
# inheriating the actual 
class mythread(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        print("my thread is created")
    def run(self): 
        print("thread is running")
        print(threading.current_thread().name)
        print(threading.current_thread().threadID)
        print(threading.active_count())
        print(threading.get_native_id())
        sample_fun(self.threadID)
        
def sample_fun(id):
    time.sleep(5)
    print(f"{id} is busy in execution ")
            
        
threadobj=mythread(101,"anil")
threadobj.start()
threadobj.join()
threads=threading.enumerate()
threadobj1=mythread(102,"sreeram")
threadobj1.start()
for i in threads:
    print(i.name)
threadobj1.join()    

            