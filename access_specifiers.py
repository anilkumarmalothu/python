class student:
   
    def __init__(self,address,name,roll_no):
        self.address=address
        self.__name=name
        self.roll_no=roll_no
    def display(self):
        print("student name",self.__name)
        print("roll_no",self.roll_no)
        print("roll_no",self.address)
    
stu=student("kdd","anil",28)   
stu.display()
stu.__name="sreeram"
print(stu.__name)
stu.display()
