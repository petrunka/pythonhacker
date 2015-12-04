class BankAccount:
    def __init__(self, name, balance, currency):
        self._name = name
        self._balance = balance
        self._currency = currency
        self._hist = ['Account was created.']

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self._name, self._balance, self._currency)

    def __int__(self):
        return int(self._balance)

    def deposit(self, amount):
        self._balance +=amount
        self._hist.append('Deposited {}{}'.format(amount, self._currency))
        self._hist.append('Balance check => {}{}'.format(self._balance, self._currency))
        

    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount<=self._balance:
            self._balance-=amount
        self._hist.append('Withdrawn {}{}'.format(amount, self._currency))
        self._hist.append('Balance check => {}{}'.format(self._balance, self._currency))
        else:
            self._hist.append('{}{} withdraw failed'.format(amount, self._currency))

    def transfer_to(self, other, amount):
        if amount<=self._balance:
            self._balance-=amount
            other._balance+=amount
            self._hist.append('Transferred {}{} to {}'.format(amount, self._currency, other._name))
        self._hist.append('Balance check => {}{}'.format(self._balance, self._currency))
        else:
            self._hist.append('{}{} transfer to {} failed'.format(amount, self._currency, other._name))

    def history(self):
        return self._hist
