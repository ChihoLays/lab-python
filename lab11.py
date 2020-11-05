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
