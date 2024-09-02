def max_of_three(num1,num2,num3):
    # if num1>num2 and num1>num3:
    #     return num1
    # elif num2>num1 and num2>num3:
    #     return num2
    # else:
    #     return num3
    return max(num1,num2,num3)
num1=int(input("enter the 1st number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
val=max_of_three(num1,num2,num3)    
print(f"max number is {val}")