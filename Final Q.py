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
#Q4
class EWallet:
    def __init__(self,ca,name,max_val):
        self.__current_amount = ca
        self.owner = name
        self.max_val = max_val
    def put_in(self,money):
        if (self.__current_amount+money) > self.max_val:
            print("Sorry, but the amount will exceed the limit.")
            return -1
        else:
            self.__current_amount += money
            print("Successfully deposit money.")
    def take_out(self,money):
        if (self.__current_amount-money) < 0:
            print("Sorry, your balance is not enough.")
            return -1
        else:
            self.__current_amount -= money
            print("Successfully withdraw money.")
    def show_current_amount(self):
        print(f"{self.owner}'s balance: {self.__current_amount} ฿")
#Q5
class SecuredEWallet(EWallet):
    def __init__(self,ca,name,max_val):
        super().__init__(ca,name,max_val)
        self.history = []
    def put_in(self,money):
        if super().put_in(money) != -1:
            self.history.append(f"Put in {money} ฿")
    def take_out(self,money):
        if super().take_out(money) != -1:
            self.history.append(f"Take out {money} ฿")
    def show_history(self):
        for log in self.history:
            print(log)
kris = SecuredEWallet(2000,"Kris",5000)
kris.put_in(500)
kris.put_in(5000)
kris.take_out(500)
kris.take_out(5000)
kris.show_current_amount()
kris.show_history()
#Q5
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
