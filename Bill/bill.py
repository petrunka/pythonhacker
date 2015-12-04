class Bill:
    def __init__(self, amount):
        self._amount = amount

    def __str__(self):
        return "A {}$ bill".format(self._amount)

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
