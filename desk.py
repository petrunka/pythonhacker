from cashdesk import Bill
from batchbill import BatchBill

class CashDesk:
    def __init__(self):
        self._amount = 0

    def take_money(self, amount):
        if isinstance(amount, BatchBill):
            self._amount+=amount.total()
        elif isinstance(amount, Bill):
            self._amount+=amount.__int__()
            

    def total(self):
        return self._amount

    def inspect(self):
        total = "We have a total of {}$ in the desk.".format(self._amount)
        total+="\nWe have the following count of bills, sorted in ascending order."
        for i in bills:
            total+="\n"+str(i)
        return total
        

values = [10,20,50,100,100,100]
bills = [Bill(value) for value in values]
batch = BatchBill(bills)
desk = CashDesk()
desk.take_money(batch)
print(desk.total())
print(desk.inspect())
desk.take_money(Bill(20))
print(desk.total())
