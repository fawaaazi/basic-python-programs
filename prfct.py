n=int(input("Enter a number:"))
r=0
m=n
for i in range(1,n):
    if((n%i)==0):
        r+=i
if(r==m):
    print("It is a perfect number")
else:
    print("It is not")
