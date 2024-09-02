class customer:
    def __init__(self,code,name,address):
        self.code=code
        self.name=name
        self.address=address
    def display(self):
        print(f"code: {self.code}\n customer name: {self.name}\n address:{self.address}")    
class corporate_customer(customer):
    def __init__(self, code, name, address,discount,offer):
        super().__init__(code, name, address)
        self.discount=discount
        self.offer=offer
    def display(self):
        super().display()
        print(f"discount: {self.discount}\n offer: {self.offer}\n")      
cust=corporate_customer(123,"anil","kdd","50%",999)
cust.display()