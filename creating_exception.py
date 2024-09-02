class invalidage(Exception):
    def __init__(self,age):
        self.age=age
    def __str__(self):
        return f"{self.age} is not valid age candiadate should have age b/w 18 to 25"
class Candidate:
    def __init__(self,name,age):
        self.name=name
        self.age=age 
    def candidatevalidation(self):
        if(self.age>=18 and self.age<=25):
            print("candiate is elgible")
        else:
            raise invalidage(self.age)
try:        
    candidate=Candidate("anil",2)
    candidate.candidatevalidation()
except invalidage  as inv:
    print(inv)
print("code execution completed")    
                       