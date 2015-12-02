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

    
