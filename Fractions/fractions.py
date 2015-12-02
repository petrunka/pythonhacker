class Fraction:

    def __init__(self, _numerator, _denominator):
        self._numerator = _numerator
        self._denominator = _denominator

    def __str__(self):
        return "{} / {}".format(self._numerator, self._denominator)

    def __repr__(self):
        return self.__str__()

    def add(self, other):
        return "{:.2f}".format((self._numerator / self._denominator) + (other._numerator / other._denominator))

    def substract(self, other):
        return "{:.2f}".format((self._numerator / self._denominator) - (other._numerator / other._denominator))

    def multiply(self, other):
        return "{:.2f}".format((self._numerator / self._denominator) * (other._numerator / other._denominator))

    def __eq__(self, other):
        return (self._numerator / self._denominator) == (other._numerator / other._denominator)

a = Fraction(1,2)
b = Fraction(2,4)
print(a.add(b))
print(a.substract(b))
print(a.multiply(b))
print(a==b)
