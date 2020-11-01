from turtle import *
from itertools import cycle
def pie_chart(data):
    num = list(set(data))  # To clear out all duplicate
    all = len(data)  # To check how long the data is
    col = cycle(['red','yellow', 'green', 'cyan', 'white', 'blue', 'mediumpurple'])
    am = [0] * len(num)  # To create a list for counting
    for i in range(len(num)):
        for j in data:
            if num[i] == j:
                am[i] += 1
    for i in range(len(am)):
        am[i] = (am[i] / all)
    total = sum(am)
    print(am)
    # draw circle size 100
    speed(0)
    goto(0, -100)
    circle(100)
    for i in range(len(num)):
        color(next(col))
        begin_fill()
        circle(100, (am[i] * 360) / total)
        temp = position()
        goto(0, 0)
        end_fill()
        setposition(temp)
    color("black")
    circle(100)
    for i in range(len(num)):  # Panel lining
        circle(100, (am[i] * 360) / total)
        temp = position()
        goto(0, 0)
        setposition(temp)
    done()

pie_chart([3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3])
