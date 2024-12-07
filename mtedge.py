r1=int(input("Enter the number of rows"))
c1=int(input("Enter the number of columns"))
A=[]
o=0
p=0
print("Enter the elements of matrix A")
for i in range(r1):
    a=[]
    for j in range(c1):
        k=int(input())
        a.append(k)
    A.append(a)
for i in A:
    print(i)
    
for i in range(r1):
    for j in range(c1):
        if(i==j):
            o+=A[i][j]
        elif((i+j)==(r1-1)):
            p+=A[i][j]

print("Sum of diagonals=",o)
print("Sum of diagonals=",p)

