#Q1
import math as m

class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def printInfo(self):
        return f"x,y coordinates = ( {self.x}, {self.y} )"


class Circle(Point):

    def __init__(self, x=0, y=0, radius=0.0):
        super().__init__(x, y)

        self.radius = float(radius)

    def area(self):
        return m.pi * (self.radius ** 2)

    def printInfo(self):
        return (f"{super().printInfo()} Radius = {self.radius:.2f} Area = {self.area():.2f}")


class Cylinder(Circle):

    def __init__(self, x=0, y=0, radius=0.0, height=0.0):
        super().__init__(x, y, radius)

        self.height = height

    def area(self):
        return 2 * super().area() + 2 * m.pi * self.radius * self.height

    def volume(self):
        return super().area() * self.height

    def printInfo(self):
        return f"{super().printInfo()} Height = {self.height:.2f} Volume = {self.volume():.2f}"

print(Point(x=1,y=2).printInfo())
print(Circle(x=5,y=6,radius=1).printInfo())
print(Cylinder(x=5,y=6,radius=1,height=1).printInfo())

#Q2
import math as m
class Calculator():

    def __init__(self, acc):

        self.acc = acc

    def set_accumulator(self, a):

        self.acc = a

    def get_accumulator(self):

        return self.acc

    def add(self, x):

        self.acc += x
        return self.acc

    def subtract(self, x):

        self.acc -= x
        return self.acc

    def multiply(self, x):

        self.acc *= x
        return self.acc

    def divide(self, x):

        if x == 0:
            return "Error : cant divided by zero"
        else:
            self.acc /= x
            return self.acc

    def print_result(self):

        return f"Result: {self.acc:.2f}"


class Sci_calc(Calculator):

    def __init__(self, acc):

        super().__init__(acc)

    def square(self):

        self.acc = super().multiply(self.acc)

        return self.acc

    def exp(self, x):

        temp = self.acc
        for i in range(1, x):
            self.acc = super().multiply(temp)

        return self.acc

    def factorial(self):

        lenacc = int(self.acc)
        fmod = 2.0

        if 0 <= self.acc <= 1:
            self.acc = 1
            return self.acc

        for i in range(2, lenacc + 1):
            if self.acc % fmod == 0 or self.acc % i == 0:
                self.acc = m.factorial(self.acc)
                break
            else:
                return "Error: cannot factorial"
            fmod += 1.0

        return self.acc

    def print_result(self):
        return f"{self.acc:.2e}"

#Q3 still need to fix
class Name:
    def __init__(self,title,fName,lName):
        self.title = title
        self.fName = fName
        self.lName = lName
    def setName(self,t,f,l):
        self.title = t
        self.fName = f
        self.lName = l
    def getFullName(self):
        print(f"{self.title}. {self.fName}")

class Date:
    def __init__(self,d,m,y):
        self.d = d
        self.m = m
        self.y = y
    def setDate(self,d,m,y):
        self.d = d
        self.m = m
        self.y = y
    def getDate(self):
        return f"{self.d:02d}/{self.m:02d}/{self.y}"
    def getDateBC(self):
        return f"{self.d:02d}/{self.m:02d}/{self.y+543}"

class Address():
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.no = houseNo
        self.st = street
        self.dt = district
        self.ct = city
        self.cn = country
        self.po = postcode

    def setAddress(self, houseNo, street, district, city, country, postcode):
        self.no = houseNo
        self.st = street
        self.dt = district
        self.ct = city
        self.cn = country
        self.po = postcode

    def getAddress(self):
        return f"House No: {self.no} Street: {self.st} District: {self.dt} City: {self.ct} Country: {self.cn} Postcode: {self.po}"

class Department():
    def __init__(self,description,manager,employeelist):
        self.des  = description
        self.man = manager
        self.elist = employeelist
    def addEmployee(self,e):
        self.elist.append(e)
        e.department = self.des
    def deleteEmpolyee(self,e):
        self.elist.remove(e)
        e.department = 'NULL'
    def setManager(self,e):
        if( type(e)==PermEmployee) and (e in self.elist):
            self.man = e
        else: return "Not a permanent employee or not in the list"
    def printinfo(self):
        return f"Department : {self.des}\tManager : {self.man.first}\tEmployeelist : {','.join(self.elist)}"

class Person(Name,Date,Address):
    def __init__ (self,title,first,last,d,m,y,houseno,street,district,city,country,postcode):
        self.name = Name(title,first,last)
        self.birthdate = Date(d,m,y)
        self.address = Address(houseno,street,district,city,country,postcode)
    def printInfo(self):
        self.name.getFullName()
        self.birthdate.getDate()
        self.address.getAddress()

class Employee(Person):
    def __init__(self,title,first,last,d,m,y,houseno,street,district,city,country,postcode,sd,sm,sy,description,manager,employeelist):
        super().__init__(title,first,last,d,m,y,houseno,street,district,city,country,postcode)
        self.startdate = Date(sd,sm,sy)
        self.department = Department(description,manager,employeelist)
    def printInfo(self):
        super().printInfo()
        self.department.printinfo()

class TempEmployee(Employee):
    def __init__(self,title,first,last,d,m,y,houseno,street,district,city,country,postcode,sd,sm,sy,description,manager,employeelist,wage):
        super().__init__(title,first,last,d,m,y,houseno,street,district,city,country,postcode,sd,sm,sy,description,manager,employeelist)
        self.wage = wage
    def printInfo(self):
        super().printInfo()
        print(f"wage: {self.wage}")

class PermEmployee(Employee):
    def __init__(self,title,first,last,d,m,y,houseno,street,district,city,country,postcode,sd,sm,sy,description,manager,employeelist,salary):
        super().__init__(title,first,last,d,m,y,houseno,street,district,city,country,postcode,sd,sm,sy,description,manager,employeelist)
        self.salary = salary
    def printInfo(self):
        super().printInfo()
        print(f"wage: {self.salary}")
