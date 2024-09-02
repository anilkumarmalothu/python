#lambda/anonymous function preferred to use for single statement expression functions
hello=lambda:print("hello")
hello()

#lambda/anonymous function 
greet=lambda message,name:message+" "+name
print(greet("good morning","anil"))



#KEY WORD ARGUMENTS
def display(name,city,/):#for only key value arguments allowed
    print(name+" "+"is staying "+" "+city)
display("chennai","anil") 
#display(city="chennai",name="anil")   


#normal passing ARGUMENTS
def display(*,name,city):#for only normal arguments allowed
    print(name+" "+"is staying "+" "+city)
#display("chennai","anil") 
display(city="chennai",name="anil")   






