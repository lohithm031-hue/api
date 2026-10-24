n=int(input("enter the number"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")

n=int(input("enter the number"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("the reversed number is",rev)