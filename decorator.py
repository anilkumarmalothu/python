import datetime

def sample_outer():
    print("sample outer function")
    
    def sampl_inner():
        print("inner function")
    return sampl_inner()

    
sample=sample_outer()



def add_message(function): #decorator
    print("hello executing the function ",datetime.datetime.now())
    def inner_fun(): #wrapper
        return function()
    return inner_fun()
@add_message
def say_hello():
    print("hello......!") 
say_hello


def greetings(function): #decorator
    
    def sample_inner(*args):#wrapper
        print("hello executing the function",datetime.datetime.now())
      
        return function(*args)
    return sample_inner


@greetings       
def say_bye(name,name1):
    print("bye "+name," "+name1)
say_bye("anil","sreeram")           
       