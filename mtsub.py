r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))
A=[]
B=[]
C=[]
print("Enter the elements of matrix A")
for i in range(r):
    a=[]
    for j in range(c):
        k=int(input())
        a.append(k)
    A.append(a)
for i in A:
    print(i)
print("Enter the elements of matrix B")
for i in range(r):
    b=[]
    for j in range(c):
        k=int(input())
        b.append(k)
    B.append(b)
C=[[0 for i in range(r)] for j in range(c)]
for i in range(r):
    for j in range(c):
        C[i][j]=A[i][j]+B[i][j]

for i in C:
    print(i)
