# num=int(input("enter the current number: "))
# print(f"the current number is {num} and the previous is {num-1} the sum is",num+num-1)

prev_num=0
for i in range(1,11):
    sum=prev_num+i
    print(f"the sum of previous number  {prev_num} and current number {i} is : ",sum)
    prev_num=i
    
