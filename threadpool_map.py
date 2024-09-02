from time import sleep,perf_counter
from concurrent.futures import ThreadPoolExecutor
import threading

def display(id):
    print(f"starting the task {id}\n")
    sleep(1)
    return f"done with the task {id}"
# start=perf_counter()
executor=ThreadPoolExecutor()
# with ThreadPoolExecutor() as executor:
    # f1=executor.submit(display,1)#returns a object called future on success and exception on failure
    # f2=executor.submit(display,2)
result=executor.map(display,[12,13])

# print(f1.result())#future object will have result() or exception()
# print(f2.result())

# fnish=perf_counter()
# print(f"the {finish-start} seconds to finish")    
for data in result:
    print(data)
    print(threading.active_count())
executor.shutdown()
for data in threading.enumerate():
    print(data.name)        