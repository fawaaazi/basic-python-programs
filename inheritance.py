class person:
    def getDetails(self):
        self.name=input("Enter name:")
        self.address=input("Enter address:")
        self.age=int(input("Enter age:"))

    def displayDetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.address)
class child:
    def __init__(self):
        self.parent=""
    def getParent(self):
        self.parent=input("Enter the name of parent")
    def displayParent(self):
        print("Parent:",self.parent)
class student(person,child):
    def studentDetails(self):
        self.ID=input("Enter ID:")

    def displayStudent(self):
        print("Name:",self.name)
        print("ID:",self.ID)
        print("Age:",self.age)  
        print("Address:",self.address)

student1=student()
student1.getDetails()
student1.studentDetails()
student1.displayStudent()     
student1.getParent()
student1.displayParent()
       