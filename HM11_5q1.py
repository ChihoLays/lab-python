import abc
from turtle import *
class Char(abc.ABC):
    def __init__(self):
        self.width = 20
    def draw(self,x,y):
        pu()
        goto(x,y)
        pd()
        setheading(0)
        pass
    def getWidth(self):
        return self.width

class Char0(Char):
    def __init__(self):
        super().__init__()
    def draw(self,x,y):
        super().draw(x,y)
        for i in range(2):
            fd(self.width)
            lt(90)
            fd(self.width * 1.5)
            lt(90)

class Char1(Char):
    def draw(self,x,y):
        super().draw(x,y)
        fd(self.width)
        bk(self.width/2)
        lt(90)
        fd(self.width * 1.5)
        lt(135)
        fd(self.width / 1.5)

class Char2(Char):
    def draw(self,x,y):
        super().draw(x,y)
        fd(self.width)
        bk(self.width)
        lt(90)
        fd(self.width * 0.75)
        rt(90)
        fd(self.width)
        lt(90)
        fd(self.width * 0.75)
        lt(90)
        fd(self.width)

class Char3(Char):
    def draw(self,x,y):
        super().draw(x,y)
        fd(self.width)
        lt(90)
        fd(self.width * 0.75)
        lt(90)
        fd(self.width)
        bk(self.width)
        rt(90)
        fd(self.width * 0.75)
        lt(90)
        fd(self.width)

class Char4(Char):
    def draw(self,x,y):
        super().draw(x+self.width,y)
        lt(90)
        fd(self.width * 1.5)
        bk((self.width*1.5)/2)
        lt(90)
        fd(self.width)
        rt(90)
        fd((self.width*1.5)/2)

class Char5(Char):
    def draw(self,x,y):
        super().draw(x,y)
        fd(self.width)
        lt(90)
        fd(self.width * 0.75)
        lt(90)
        fd(self.width)
        rt(90)
        fd(self.width * 0.75)
        rt(90)
        fd(self.width)

class Char6(Char):
    def draw(self,x,y):
        super().draw(x,y)
        for i in range(2):
            fd(self.width)
            lt(90)
            fd((self.width * 1.5) / 2)
            lt(90)
        lt(90)
        fd(self.width*1.5)
        rt(90)
        fd(self.width)

class Char7(Char):
    def draw(self,x,y):
        super().draw(x,y+(self.width*1.5))
        fd(self.width)
        goto(x,y)

class Char8(Char):
    def draw(self,x,y):
        super().draw(x,y)
        for i in range(4):
            fd((self.width * 1.5) / 2)
            lt(90)
        goto(x,y+(self.width * 1.5) / 2)
        for i in range(4):
            fd((self.width * 1.5) / 2)
            lt(90)

class Char9(Char):
    def draw(self,x,y):
        super().draw(x+(self.width),y)
        goto(x+(self.width),y+(self.width * 1.5) / 2)
        goto(x,y+(self.width * 1.5) / 2)
        for i in range(2):
            fd(self.width)
            lt(90)
            fd((self.width * 1.5) / 2)
            lt(90)

def drawNum(usnum):
    ht()
    speed(0)
    usnum = str(usnum)
    posX = 0
    num = {"0": Char0(), "1": Char1(), "2": Char2(), "3": Char3(),
           "4":Char4(), "5": Char5(),"6": Char6(), "7": Char7(),
           "8": Char8(), "9": Char9()}
    for char in usnum:
        if char in num:
            num[char].draw(posX, 0)
            posX += 20 * 1.25
    done()

drawNum(123456789)
