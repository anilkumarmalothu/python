def say_hello():    #function definition
    print("hello anil")
say_hello() #function call
def say_good_mrng(name):
    print("good morning" + "  "+name)
say_good_mrng("anil")    
def greetings(message,name):
    return message+" "+name  #function returning the arguments
print(greetings("happy birthday","bala"))


store=greetings("hi","anil")
print(store)