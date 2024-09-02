#example of producer and one consumer with threads
from time import sleep
from random import random
from threading import Thread
from queue import Queue


#producer task put the data into shared queue

def producer(queue):
    print("producer :running")
    #generate items
    
    for i in range(10):
        value=random()
        sleep(value)
        item=(i,value)
        queue.put(item)
        print(f"producer added {item}")
    queue.put(None)
    print("producer:done") 
#consumer function to consume the queue start    
def consumer(queue):
    print("consumer :running")
    
    while True:
        item=queue.get()
        if item is None:
            break
        sleep(item[1])
        print(f"consumer got {item} ")
    print("consumer :done")

#craete a shared queue
queue=Queue()
#start consumer thread
consumer_thread=Thread(target=consumer,args=(queue,))
consumer_thread.start()
#start a producer
producer_thread=Thread(target=producer,args=(queue,))
producer_thread.start()
#wait until all thread to finish execution
producer_thread.join()
consumer_thread.join()


           