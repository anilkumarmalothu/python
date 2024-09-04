import threading 
#threading is builtin package in python in which "Thread" class contains  which is used for creating thread

def my_count(): # my count is generator using yield it returns data more than one time as you call by __next__ function call
    i = 0
    while True:
        i += 1
        yield i
# class which is my counter which exactly  works same as the my_count generator 
class MyCounter:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        self.i += 15
        return self.i
# the "func" is a generator return value
 #function which is passed to thread   
def loop(func, n): 
   #loop which repeats n time and prints the c1.__next__() value and c2.next() value 
    for i in range(n): 
        print(f"value is {func} \n") 
#these function contains default arguments which are consider while nothing is passed in function call
#the argument "f" is a generator return value here 
def sample(f, repeats=1000, nthreads=10):
   
    # create threads
    #list comprehension which stores two threads and which creates two threads ,creation of threads totally which depends on nthreads arguments
    threads = [threading.Thread(target=loop, args=(f, repeats)) for i in range(nthreads)]

    # start threads
    for t in threads: 
        t.start()  

    # wait for threads to finish
    for t in threads:
        t.join()

def main():
    c1 = my_count() #creating a generator 
    c2 = MyCounter() #creating a instance of my_counter class 

    # call c1.next
    sample(c1.__next__(), repeats=10, nthreads=2) 
    print( "c1", c1.__next__()) #as we are calling __next__ another time will returns the next value in generator 
    print( "c1", c1.__next__())
    # call c2.next
    sample(c2.next(), repeats=10, nthreads=2) # calling sample() function by passing respective arguments value to sample 
    print( "c2", c2.next()) # as we are calling __next__ another time it it adds the +15 

if __name__ == "__main__": #from the main function exection start as these main these condition true
    main()       #calling main function
