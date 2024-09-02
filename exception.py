try:   # the code by which we are expecting error can be written in try block 
    print("enter two numbers: ")
    num1=int(input("enter first number :"))
    num2=int(input("enter the second number: "))
    result=num1/num2
    print(result)
except ZeroDivisionError as zde: # these an error handling block
    print(zde)
except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)
else: #else block only executed when try block executed successfully
    print("try block got successsfully")
finally:
    print("finally called")                    