import abc
class StationaryGood(abc.ABC):
    def __init__(self,amount,price):
        self.amount = amount
        self.price = price
        self.cost = price * amount
    def get_price(self):
        return self.cost

class Magazine(StationaryGood):
    def __init__(self,amount,price):
        super().__init__(amount,price)
class Book(StationaryGood):
    def __init__(self,amount,price):
        super().__init__(amount,price)
    def get_price(self):
        return  (super().get_price() * 0.9)
class Ribbon(StationaryGood):
    def __init__(self,length):
        super().__init__(length,5)

def getTotalCost(basket):
    sum = 0
    for item in basket:
        sum += item.get_price()
    return sum

basket = [Magazine(3,70),Book(2,200),Ribbon(10)]
print(f"Total: {getTotalCost(basket)} Baht")
