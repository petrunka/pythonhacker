class Panda:
    def __init__(self, _name, _age, _weight):
        self._name = _name
        self._age = _age
        self._weight = _weight

    def eat(self, amount):
        self._weight+=amount

    def sleep(self):
        self._age+=1

    def __get_age(self):
        return self._age

    def __get_weight(self):
        return self._weight

    def __str__(self):
        return "I am {} and I am a proud Panda".format(self._name)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._age ==other._age

    def __hash__(self):
        return hash(self._name+str(self._age))


vladimir = Panda("Vladimir", 22, 77)
rado = Panda("Rado", 24, 110)
vladimir.sleep()
vladimir.eat(4)
vladimir.sleep()
vladimir.eat(12)
print(str(vladimir))
print(repr(vladimir))
print(vladimir==rado)
print(hash(vladimir))
