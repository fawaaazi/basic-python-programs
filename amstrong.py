n=int(input("enter no:"))
temp=n
sum=0
while(temp>0):
    k=temp%10
    sum=sum+k**3
    temp=temp//10

if(sum==n):
    print("amstrong  no")
else:
    print("not")
