"""
To this point I will assume that u have already understand how normal class works
Now I will continue about some advance concept such as private attr and Inheritance

Lets start with private attr
I will explain in the most simplest form
If you work on a group project
How will you or your friends know that they shouldn't change things in class?
if _ in front of attr or method  -> you shouldn't edit or access the data if not necessary
elif __ in front of attr or method -> If u r not the project manager then you should never touch it ever.
__ -> Private
__(Properties/Var/Attr) -> Private Properties/Var/Attr
__(Method) -> Private Method

Next topic -> Inheritance
Lets say that if you want to create more than 2 class with many similarity and only a few difference
Normally you would create the first class then the other class by copy and paste using the first one
However, for a very large project it is not smart to do that
To make you understand easier
I will create a Dog class
by using the manual way
then I will be showing you how it is easier to create it using inheritance
"""
class Bulldog:
    def __init__(self,name,age):
        self.animal_type = "Dog"
        self.species = "Bull dog"
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: *barked*")


class GoldenRetriever:
    def __init__(self, name, age):
        self.animal_type = "Dog"
        self.species = "Golden Retriever"
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: *barked*")


class Greyhound:
    def __init__(self, name, age):
        self.animal_type = "Dog"
        self.species = "Greyhound"
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: *barked*")

# As u can see this writing it this way is not efficiency af
# Lets try using inheritance
# class the Parents class first
class Dog:
    def __init__(self, name, age,spiecies):
        self.animal_type = "Dog"
        self.species = spiecies
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name}: *barked*")
# class the child class
class Bulldog(Dog):  # Inside the () is where the class will inherit all the attr and method from
    def __init__(self, name, age,spiecies):
        super().__init__(name,age,"Bull dog")
class GoldenRetriever(Dog):
    def __init__(self, name, age,spiecies):
        super().__init__(name,age,"Golden Retriever")
class Greyhound(Dog):
    def __init__(self, name, age,spiecies):
        super().__init__(name,age,"Greyhound")

"""
Exercise3:
Write Car class that contains the following properties and method
Car Properties:
1. Owner
2. Brand
3. Color
4. License plate ID
5. Year
6. Speed
Method:
travel(time) -> display out the traveled distance according to the speed of each type of car, but time >= 0
change_speed(new_speed) -> Change the speed of the car

Then create the following class by inheriting from the Car class
BMW
Additional method:
dis_info -> Display all info as follow
'This is a bmw car
Owner:Kris Color:Black ID:PYQT5 Year:2012'
Nissan
Additional method:
dis_info -> Display all info as follow
'Owner:Jack Brand:Nissan Color:White ID:COVID-19 Year:2019'
"""
