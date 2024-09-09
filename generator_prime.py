def prime(range_val):
    
    for i in range(2,range_val+1):
        cnt=0
        for j in range(2,i+1//2):
            if(i%j==0):
                cnt+=1
        if cnt==0:
            yield i


val=int(input("enter the value of range:"))
prime_no=prime(val)
print("the prime no are :")
for i in prime_no:
    print(i)                    