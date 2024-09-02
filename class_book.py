class Book:
    
    def __init__(self,isbn,title,author,price):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print("the isbn number is :",self.isbn)
        print("the isbn number is :",self.title)
        print("the isbn number is :",self.author)
        print("the isbn number is :",self.price)
    def __del__(self):
        print("destructor invoked")    
b=Book("123","buckarroo","steeve",123)   
b.display()     