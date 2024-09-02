#operator overloadiong
 
class Distance:
    def __init__(self,dc=12):
        self.dc=dc
    def __add__(self,obj2):  # operator overloading for "+" operator
         return self.dc+obj2.dc
    def __str__(self): # we use this instead of display function inbuild function
        return f"distance : {self.dc}"
dobj1=Distance()
dobj2=Distance()
print(dobj1)
print(dobj1+dobj2)        