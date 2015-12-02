class Bill:
    def __init__(self, _amount):
        self._amount = _amount

    def __str__(self):
        return "A {}$ bill".format(self._amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self._amount)

    def __eq__(self, other):
        return self._amount == other._amount

    def __hash__(self):
        return int(self._amount)

    def _get_amount(self):
        return self._amount

class BatchBill:
    def __init__(self, _bills):
        self._bills = _bills

    def __len__(self):
        return len(self._bills)

    def total(self):
        amount = 0
        for i in range(0, len(self._bills)):
            amount+=self._bills[i].__int__()
        return amount


    def __getitem__(self, index):
        return self._bills[index]

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


a = Bill(11)
b = Bill(11)
c = Bill(7)
money_holder = {}
money_holder[a]=1
if b in money_holder:
    money_holder[b]+=1
print(money_holder)
print(a)
print(int(a))
print(str(a))
print(a==b)
print(a==c)
values = [2,5,10,20]
bills = [Bill(value) for value in values]
batch = BatchBill(bills)
print(batch.total())
print(batch.__len__())
print(batch.__getitem__(1))
for bill in batch:
    print(bill)
values = [10,20,50,100,100,100]
bills = [Bill(value) for value in values]
batch = BatchBill(bills)
desk = CashDesk()
desk.take_money(batch)
print(desk.total())
print(desk.inspect())
desk.take_money(Bill(20))
print(desk.total())
    
