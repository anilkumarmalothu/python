from time import sleep,perf_counter
from concurrent.futures import ThreadPoolExecutor

def display(id):
    print(f"starting the task {id}")
    sleep(1)
    return f"done with the task {id}"
start=perf_counter()
with ThreadPoolExecutor() as executor:
    f1=executor.submit(display,1)#returns a object called future with result on success and exception on failure
    f2=executor.submit(display,2)

print(f1.result())#future object will have result() or exception()
print(f2.result())

finish=perf_counter()
print(f"the {finish-start} seconds to finish")    
