import threading

num = 0

def increment():
    global num
    for i in range(1000000):
        num += 1
   

def decrement():
    global num
    for i in range(1000000):
        num -= 1
   

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)

t1.start()
t2.start()
t1.join()
t2.join()

print("num result : %s" % num)