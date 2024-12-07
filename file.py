import pickle
with open("str.txt","w")as f:
    n=int(input("how many no:"))
    for i in range(n):
        k=input()
        f.write(k)
        f.write("\n")
with open("str.txt","r")as f:
    sq=[]
    no=[]
    for i in range(n):
        z=int(f.readline().strip())
        no.append(z)
        sq.append(z**2)
with open("text.pkl","wb")as f:
    pickle.dump(no,f)
with open("result.txt","w") as f:
    f.write(str(no))   
    f.write("\n")
    f.write(str(sq))
f=open("text.txt","w")
f.write("fawas")
f.close()



