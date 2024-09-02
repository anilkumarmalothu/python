class employee:
    """
    class to work with employee details
    """
    employee_cnt=0
    
    def __init__(self,emp_name,emp_id):
        self.emp_name=emp_name
        self.emp_id=emp_id
        employee.employee_cnt+=1
    def display(self):
        print("hello ",self.emp_name,self.emp_id)
        # @classmethod keyword is used convert the particular method to class method we need to use the self parameter while using these method .
    @staticmethod #by using @staticmethod we can avoid the usage of self parameter in arguments
    def show_cnt():
        print("count : ",employee.employee_cnt)
    # empcnt=classmethod(show_cnt)   


         
emp=employee("anil","PT005")
emp.display()            
emp=employee("sriram,","PT005")
emp.display()  
emp.show_cnt()

# employee.empcnt()

print(employee.employee_cnt)    
print(employee.__doc__)# displays the comment entry which you entered during the creation of class
print(employee.__name__) # it displays the name of the class which u working with
print(employee.__module__) # it displays the module in which u writing code
print(employee.__base__) # it displays base class
employee.show_cnt()