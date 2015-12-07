from car import Car
class Driver:
    def __init__(self, name, car):
        self._name = name
        self._car = car
        self._bad_day = 2

    def __str__(self):
        return "{} has a car {}".format(self._name, self._car)

    def __repr__(self):
        return self.__str__()
