#Q1
def find_member_positions(val,lst):
    pos = []
    for i in range(len(lst)):
        if val == lst[i]:
            pos.append(i)
    if pos == []:
        return 0
    else:
        return pos
print(find_member_positions(2,[2,5,3,2,4]))
print(find_member_positions(1,[2,5,3,2,4]))
#Q2
routes = {"i":("j",4.0),"a":("b",3.4),"j":("k",6.0),"c":("d",5.6),"b":("c",4.0)}
def find_route(start,routes):
    keep= [start]
    sum_dis = 0.0
    while start != 'd' and start != 'k':
        start = routes[start]
        keep.append(start[0])
        sum_dis += start[1]
        start = start[0]
    return (keep,sum_dis)
print(find_route("a",routes))
print(find_route("b",routes))
#Q3
def recur_find_route(start,routes,sum_dis = 0.0):
    if start == 'd' or start == 'k':
        return sum_dis
    else:
        start = routes[start]
        sum_dis += start[1]
        start = start[0]
        return recur_find_route(start,routes,sum_dis)
print(recur_find_route("a",routes))
print(recur_find_route("b",routes))
