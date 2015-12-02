class Bill:
    def __init__(self, amount):
        self._amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.$amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self._amount)

    def __eq__(self, other):
        return self._amount == other._get_amount()

    def __hash__(self):
        return int(self._amount)

    def _get_amount(self):
        return self._amount

class BatchBill:
    def __init__(self, bills):
        self._bills = bills

    def __len__(self):
        return len(self._bills)

    def total(self):
        return sum([bill.get_amount() for bill in self._bills])


    def __getitem__(self, index):
        return self._bills[index]

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
