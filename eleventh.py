class Person:
    def __init__(self):
        pass
    def getInfo(self,name,age):
        self._name = name
        self.age = age
    def printInfo(self):
        print(self.age)
class Employee:
    def __init__(self):
        pass
    def getInfo(self,eid,sal):
        self.e = eid
        self.s = sal
    def printInfo(self):
        print(self.e,self.s)
    
class Office(Employee,Person):
    def __init__(self):
        pass
    def getInfo(self,n,y):
        Person.getInfo(Person,"Gopal","28")
        Employee.getInfo(Employee,"01","28000")
        self.n = n
        self.y = y
    def printInfo(self):
        Person.printInfo(Person)
        Employee.printInfo(Employee)
        print(self.n,self.y,Person._name)

class demo(Office):
    def __init__(self):
        print("Demo")
        
o = demo()
o.getInfo("GB Tech",2014)
o.printInfo()
