#generator
def sample():
    yield "one"
    yield "two"
my_generator=sample()    
print(my_generator.__next__()) 
print(my_generator.__next__())
my_list=(i*i for i in range(1,10))
print(my_list.__next__())
print(my_list.__next__())
print(my_list.__next__())
print(my_list.__next__())
print(my_list.__next__())
print(my_list.__next__())
print(my_list.__next__())
print(my_list.__sizeof__())
   
   