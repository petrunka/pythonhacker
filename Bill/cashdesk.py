from bill import Bill
from batchbill import BatchBill
class CashDesk:
    def __init__(self):
        self.cash = []

    def take_money(self, amount):
        self.cash.append(amount)            

    def total(self):
        return sum([obj.total() for obj in self.cash])        

    def inspect(self):
        total = "We have a total of {}$ in the desk.".format(self._amount)
        total+="\nWe have the following count of bills, sorted in ascending order."
        for i in bills:
            total+="\n"+str(i)
        return total

