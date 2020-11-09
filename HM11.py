#Q1
from datetime import datetime
class Clock:
    def __init__(self):
        now = datetime.now()
        self.hh = int(now.strftime("%H"))
        self.mm = int(now.strftime("%M"))
        self.ss = int(now.strftime("%S"))
    def format_time(self):
        if self.ss >= 60:
            self.ss %= 60
            self.mm += 1
            if self.mm >= 60:
                self.mm %= 60
                self.hh += 1
                if self.hh > 23:
                    self.hh %= 24
    def run(self):
        self.ss += 1
        self.format_time()
    def setTime(self,h,m,s):
        self.hh = h
        self.mm = m
        self.ss = s
        self.format_time()
    def get_time(self):
        return f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}"

class AlarmClock(Clock):
    def __init__(self,ahour,amin,asec,aoorf):
        super().__init__()
        self.alarm_hh = ahour
        self.alarm_mm =amin
        self.alarm_ss = asec
        self.alarm_on_off = aoorf
    def setAlarmTime(self,h,m,s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s
        if self.alarm_ss >= 60:
            self.alarm_ss %= 60
            self.alarm_mm += 1
            if self.alarm_mm >= 60:
                self.alarm_mm %= 60
                self.alarm_hh += 1
                if self.alarm_hh > 23:
                    self.alarm_hh %= 24
    def alarm_on(self):
        self.alarm_on_off = True
    def alarm_off(self):
        self.alarm_on_off = False
    def run(self):
        super().run()
        print(f"Current time: {super().get_time()}")
        if self.alarm_on_off == True and self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss:
            print(f"Alarmed:\n{super().get_time()}")
            exit(0)

test = AlarmClock(23,57,00,True)
print(f"Current time: {test.get_time()}")
test.setTime(23,56,59)
test.run()

#Q2 base Q
import turtle
def RobotBattle():
    # robotList stores the list of robots in the battle
    robotList = []

    while True:
        #Clear the screen and draw the robots
        turtle.clear()
        for robot in robotList:
            robot.draw()
        #Display the satatus of each robot
        print("==== Robots ====")
        i=0
        for robot in robotList:
            print(f"{i} : ")
            robot.displayStatus()
            i+1
        print("===============")

        #Ask which robot to command or to create a new robot
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robot to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)
        #Delete all the robots with health <= 0 from the list
        i = 0
        for robot in robotList:
            if(robot.health <= 0):
                del robotList[i]
            i += 1

class Robot(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.energy = 100

    def move(self,x,y):
    # Your code

    def draw(self):
    # Your code

    def displayStatus(self):
        print(f"x= {self.x} y= {self.y} health= {self.health} energy= {self.energy}")

    def command(self,robotList):
        print("Possible action: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX,newY)

class MedicBot(Robot):
    # Your code

class StrikerBot(Robot):
    # Your code
   
#Q2 already code
import turtle
from math import sqrt
def RobotBattle():
    # robotList stores the list of robots in the battle
    robotList = [MedicBot(),StrikerBot(),Robot()]

    while True:
        #Clear the screen and draw the robots
        turtle.clear()
        for robot in robotList:
            robot.draw()
        #Display the satatus of each robot
        print("==== Robots ====")
        i=0
        for robot in robotList:
            print(f"{i} : ")
            robot.displayStatus()
            i+=1
        print("===============")

        #Ask which robot to command or to create a new robot
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit\n")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robot to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot\n")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)
        #Delete all the robots with health <= 0 from the list
        i = 0
        for robot in robotList:
            if(robot.health <= 0):
                del robotList[i]
            i += 1

class Robot(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.health = 100
        self.energy = 100

    def move(self,newX,newY):
        self.x = newX
        self.y = newY

    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y-5)
        turtle.pendown()
        turtle.circle(5)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()


    def displayStatus(self):
        print(f"x= {self.x} y= {self.y} health= {self.health} energy= {self.energy}")

    def command(self,robotList):
        print("Possible action: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX,newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()
    def heal(self,r):
        if self.energy >= 20:
            distance= sqrt((pow((self.x-r.x),2)) + (pow((self.y-r.y),2)))
            if distance <= 10:
                self.energy -= 20
                r.health += 10
    def command(self,robotList):
        choice = input("Enter your order, 'm' to move the robot, 'h' to heal other robot in the robotList\n")
        if choice == "m":
            super().command(robotList)
        elif choice == "h":
            print("==== Robots ====")
            i = 0
            for robot in robotList:
                print(f"{i} : ")
                robot.displayStatus()
                i += 1
            print("===============")
            n = int(input("Which robot will be healed:"))
            if n in range(len(robotList)):
                self.heal(robotList[n])
    def draw(self):
        super().draw()
        turtle.penup()
        turtle.goto(self.x-(5/6),self.y-(15/6))
        turtle.pendown()
        for i in range(4):
            turtle.fd(10/6)
            turtle.left(90)
            turtle.fd(10/6)
            turtle.right(90)
            turtle.fd(10/6)
            turtle.left(90)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5
    def strike(self,r):
        if self.energy >= 20 and self.missile > 0:
            distance = sqrt((pow((self.x - r.x), 2)) + (pow((self.y - r.y), 2)))
            if distance <= 10:
                self.energy -= 20
                self.missile -= 1
                r.health -= 50
    def displayStatus(self):
        super().displayStatus()
        print(f"missile = {self.missile}")

    def command(self,robotList):
        choice = input("Enter your order, 'm' to move the robot, 's' to strike other robot in the robotList\n")
        if choice == "m":
            super().command(robotList)
        elif choice == "s":
            print("==== Robots ====")
            i = 0
            for robot in robotList:
                print(f"{i} : ")
                robot.displayStatus()
                i += 1
            print("===============")
            n = int(input("Which robot will be strike:"))
            if n in range(len(robotList)):
                self.strike(robotList[n])
    def draw(self):
        super().draw()
        turtle.penup()
        turtle.goto(self.x, self.y -(5/2))
        turtle.pendown()
        turtle.left(45)
        for i in range(4):
            turtle.fd((25/6))
            turtle.left(90)
        turtle.left(-45)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

turtle.speed(0)
RobotBattle()
turtle.done()


#Q3
from turtle import *

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def spawn(self):
        penup()
        goto(0, 0)
        setheading(0)
        pendown()
    def draw(self):
        penup()
        goto(self.x,self.y-0.5)
        pendown()
        begin_fill()
        circle(1)
        end_fill()
        self.spawn()
    def get_coor(self):
        return f"({self.x},{self.y})"

class Rectangle2D:
    def __init__(self,width,height,center):
        self.height = height
        self.width = width
        self.center = center
    def draw(self):
        x = self.center.x
        y = self.center.y
        penup()
        goto(x - (self.width/2),y- (self.height/2))
        pendown()
        goto(x + (self.width/2), y- (self.height/2))
        goto(x + (self.width/2), y + (self.height/2))
        goto(x - (self.width/2), y + (self.height/2))
        goto(x - (self.width/2), y - (self.height/2))

def getRectangle(points):
    coor_x = []
    coor_y = []
    all_coor = []
    for i in range(0,len(points),2):
        all_coor.append(Point(points[i],points[i+1]))
        coor_x.append(points[i])
        coor_y.append(points[i+1])
    coor_y.sort()
    coor_x.sort()
    width = coor_x[-1] - coor_x[0]
    height = coor_y[-1] - coor_y[0]
    center = Point(coor_x[0]+(width/2),coor_y[0]+(height/2))
    return [Rectangle2D(width,height,center),all_coor]

usin = input("Enter the points: ").split()
usin = list(map(float,usin))
r2d = getRectangle(usin)
speed(0)
r2d[0].draw()
for i in r2d[1]:
    i.draw()
print(f"The bounding rectangle is centered at {r2d[0].center.get_coor()} with width {r2d[0].width:.1f} and height {r2d[0].height:.1f}")
done()

#input 1.0 2.5 3 4 5 6 7 8 9 10
#input 10.0 25 30 40 50 60 70 80 90 100
