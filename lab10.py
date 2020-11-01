def name_list():
    lst = []
    i = 0
    while True:
        i += 1
        x = input(f"Enter name {i}: ")
        if x != '':
            lst.append(x)
        elif x == '':
            break
    return lst

def my_count(lst):
    count_pint = 0
    for i in lst:
        if i >= 0:
            count_pint -= 1
    return count_pint



list1 = [3,6,6,3,7,2,0,1,5,4]
def remove_the_thirds(x):
    count = [i for i in range(0,len(x),3)]
    count.remove(0)
    print(count)
remove_the_thirds(list1)
print(list1)

from turtle import *
def draw_rec(n):
    left(90)
    for i in range(2):
        fd(n*20)
        right(90)
        fd(10)
        right(90)
    setheading(0)

def draw_graph(count_list,num_list):
    speed(0)
    left(90)
    fd(max(count_list)*20)
    fd(20)
    stamp()
    fd((-max(count_list)*20)-20)
    right(90)
    for i in range(len(count_list)):
        fd(20)
        draw_rec(count_list[i])
        fd(10)
    fd(20)
    stamp()
    penup() #write each character
    goto(0,0)
    setheading(0)
    right(90)
    fd(20)
    right(-90)
    for i in range(len(num_list)):
        fd(20)
        pendown()
        write(num_list[i],font=("Arial", 14, "normal"))
        penup()
        fd(10)
    goto(9999,0) # hide cursor
    done()
x =[1,2,2,1,3,4,6,5,3,4,5,6,4,3,5,4,5,3,4,4,3,3,4,3,3,4,4,4,11,11]
def histogram(data):
    num = list(set(data))
    all = len(data)
    am = [0] * len(num)
    for i in range(len(num)):
        for j in data:
            if num[i] == j:
                am[i] += 1
    for i in range(len(am)):
        am[i] = (am[i]/all) * 10
    draw_graph(am,num)

histogram(x)
def get_the_difference(lst1,lst2):
    x = []
    for i in lst1:
        if i not in lst2:
            x.append(i)
    for i in lst2:
        if i not in lst1:
            x.append(i)
    return x
print(get_the_difference([3,1,1,1,2,7],[4,1,1,2,2,5]))

def my_sort(lst):
    l = []
    for i in range(len(lst)):
        if i == 0:
            l.append(lst[i])
        else:
            if lst[i] > l[-1]:
                l.append(lst[i])
            elif lst[i] < l[0]:
                l.insert(0,lst[i])
            else:
                for j in range(len(l)):
                    if lst[i] < l[j]:
                        l.insert(j,lst[i])
                        break
    return l
print(my_sort([6,4,2,1,4]))

def merge(lst1,lst2):
    for i in lst2:
        lst1.append(i)
    lst1 = my_sort(lst1)
    return lst1
lst1 = list(map(int,input("Enter list1: ").split()))
lst2 = list(map(int,input("Enter list2: ").split()))
new = list(map(str,merge(lst1,lst2)))
print(f"The merged list is {' '.join(new)}")

#1 5 16 61 111
# 2 4 5 6
