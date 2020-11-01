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


def bubble_sort(lst):
    num = len(lst)
    for i in range(num):
        for j in range(0, num - i - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

test = [3,2,9,7,8,1]
bubble_sort(test)
print(test)

def my_union(lst1,lst2):
    temp = []
    for i in lst1:
        temp.append(i)
    for i in list2:
        if i not in temp:
            temp.append(i)
    return temp
def my_intersection(lst1,lst2):
    temp = []
    for i in lst1:
        if i in lst2:
            temp.append(i)
    return temp
def my_difference(lst1,lst2):
    temp = []
    for i in lst1:
        if i not in lst2:
            temp.append(i)
    return temp
list1 = [3,1,2,7]
list2 = [4,1,2,5]
print(my_union(list1,list2))
print(my_intersection(list1,list2))
print(my_difference(list1,list2))
