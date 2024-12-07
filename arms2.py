n=int(input("Enter the number:"))
s=n
r=0
while(n>0):
    d=n%10
    r=r+d**3
    n=n//10
if(s==r):
    print("it is armstrong")
else:
    print("it is not")
    

