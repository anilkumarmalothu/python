num=int(input("enter the number to check it is plaindrome:"))
temp=num
summation=0
while num:
    rem=num%10
    summation=summation*10+rem
    num/=10
if(temp==summation):
    print("its a palindrome")
else:
    print("its not a palindrome")    