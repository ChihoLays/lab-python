#Q1
from turtle import *
import abc

class TwoDShape(abc.ABC):
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self,length):
        self.length = length
    def draw(self):
        fd(self.length)

class Rectangle(TwoDShape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def draw(self):
        for i in range(2):
            fd(self.width)
            left(90)
            fd(self.height)
            left(90)
class Circle(TwoDShape):
    def __init__(self,radius):
        self.radius = radius
    def draw(self):
        circle(self.radius)

class Square(TwoDShape):
    def __init__(self,side):
        self.side = side
    def draw(self):
        for i in range(4):
            fd(self.side)
            left(90)

item = [Rectangle(100,50),Line(200),Circle(50),Line(200),Circle(100),Square(50)]
for i in item:
    i.draw()
done()

#Q2
import abc

class Transportation(abc.ABC):
    def __init__(self, st, en, d):
        self.st = st
        self.en = en
        self.d = d
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self,st,en,d):
        super().__init__(st, en, d)
    def find_cost(self):
        return 0
class Taxi(Transportation):
    def __init__(self,st,en,d):
        super().__init__(st, en, d)
    def find_cost(self):
        return (40 * self.d)
class Train(Transportation):
    def __init__(self,st,en,d,s):
        super().__init__(st, en, d)
        self.sta = s
    def find_cost(self):
        return (5 * self.sta)

kmitl = "KMITL"
kmitlscb = "KMITL SCB Bank"
ladsta = "Ladkrabang Station"
paya = "Pyathai Station"
bricon = "The British Council"

item = [Walk(kmitl,kmitlscb,0.6),Taxi(kmitlscb,ladsta,5),Train(ladsta,paya,40,6),Taxi(paya,bricon,3)]
for i in item:
    print(i.find_cost())
