from cashdesk import Bill

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

values = [2,5,10,20]
bills = [Bill(value) for value in values]
batch = BatchBill(bills)
print(batch.total())
print(batch.__len__())
print(batch.__getitem__(1))
for bill in batch:
    print(bill)
