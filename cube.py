num=int(input("enter the number to find cube"))

square=num**num
cube=square*num
print(f"the cube of {num} is {cube}")


cube=lambda num1:(num1**3)
print(cube(2))