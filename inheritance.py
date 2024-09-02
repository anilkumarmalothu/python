class employee:
    """
    class to work with employee details
    """
    employee_cnt=0
    
    def __init__(self,emp_name="anil",emp_id="123"):
        self.emp_name=emp_name
        self.emp_id=emp_id
        employee.employee_cnt+=1
        print("parent class invoked")
    def display(self):
        print("hello ",self.emp_name,self.emp_id)
    def show_cnt():
        print("count : ",employee.employee_cnt)
    # empcnt=classmethod(show_cnt)   

class permenantEmployee(employee):
    def __init__(self):
        super().__init__("venu","1235")   
        self.benefits="medicals,pf,insurance"
        print("derived class constructor invoked")
    def display(self):
     super().display()
     print("the benfits",self.benefits)    
         
emp=employee("anil","PT005")
emp.display()            
emp=employee("sriram,","PT005")
emp.display()  

emp1=permenantEmployee()
emp1.display()


