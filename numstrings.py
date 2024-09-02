num=int(input("enter the number : "))
string=''
while num:
    rem=num%10
    string=str(""+rem)
    num/=10
print(string)    