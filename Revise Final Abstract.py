"""
Before u start learning about abstract class.
I recommend u to understand the concept of using inheritance class before hand.

What is abstract class?
By definition, a class is called an Abstract class if it contains one or more abstract methods.
What is an abstract method?
An abstract method is a method that is declared, but contains no implementation.
Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.

However, I believe that many people will think, 'What in the actual fuck does it mean?'
To make it simpler and imagine abstract class as a blue print for their child class
Why abstract class?
It allows you to create a set of methods that must be created within any child classes built from the abstract class.
Lets look at some example to get a better understanding.
"""

# Abstract Example
import abc
class Shape2D(abc.ABC):
    def get_area(self):  # Declare for child class to have the same method
        pass  # Does not do anything

class Triangle(Shape2D): # Declare that Shape2D is its parent
    def __init__(self,height,base):  # Add
        self.height = height
        self.base = base
    def get_area(self): return (self.height * self.base)  # Modify

class Circle(Shape2D): # Declare that Shape2D is its parent
    def __init__(self, r): self.radius = r  # Add
    def get_area(self): return (3.14 * (self.radius**2))  # Modify

class Rectangle(Shape2D): # Declare that Shape2D is its parent
    def __init__(self, width, length):  # Add
        self.width = width
        self.length = length
    def get_area(self): return (self.width * self.length)  # Modify

class Square(Shape2D): # Declare that Shape2D is its parent
    def __init__(self, side): self.side = side  # Add
    def get_area(self): return self.side**2  # Modify

"""
Next topic -> Polymorphism
What is Polymorphism?
By definition, Polymorphism is taken from the Greek words Poly (many) and morphism (forms). 
It means that the same function name can be used for different types. This makes programming more intuitive and easier.

In my opinion, polymorphism is exactly like abstract class but just it want the same name for the method.
"""

# Example polymorphism
class Bird: # Parent class
    def intro(self):
        print("There are different types of birds")
    def flight(self):
        print("Most of the birds can fly but some cannot")
class parrot(Bird):
    def flight(self):  # Same name as parent class
        print("Parrots can fly")
class penguin(Bird):
    def flight(self):  # Same name as parent class
        print("Penguins do not fly")

"""
Summary:
Polymorphism vs Abstract class
1. Both of these are concept and code technique
2. There is only a slight different in theory
3. In action they are the same
"""

"""
For the exercise you can do the question in the final.
If you want to check whether its correct please contact me.
"""
