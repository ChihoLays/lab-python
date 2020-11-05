import math as m

class Point(object):

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

import math as m
class Calculator(object):

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
