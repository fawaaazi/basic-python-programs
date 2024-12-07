class student:
    def __init__(self):
        self.name=""
        self.age=0
        self.id=0
        self.address=""

    def getDetails(self):
        self.name=input("Enter name:")
        self.age=int(input("Enter age:")) 
        self.address=input("Enter address:")
        self.id=int(input("Enter id:"))

    def printDetails(self):
        print("Name:",self.name)  
        print("Address:",self.address)
        print("Age:",self.age)
        print("ID:",self.id)
    def changeAddress(self):
        self.address=input("Enter new address:")
obj1=student()  
obj2=student()
print("Enter details of student1:")
obj1.getDetails()
print("Enter details of student2:")
obj2.getDetails()
obj1.printDetails()
obj2.printDetails()
ch=input("Do you want to change address(y/n):")
if(ch=='y'):
    obj1.changeAddress()
    obj1.printDetails()


