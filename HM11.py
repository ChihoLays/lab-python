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
            print(f"Alarmed\n{super().get_time()}")
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
