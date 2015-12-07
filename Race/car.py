class Car:
    def __init__(self, car, model, max_speed):
        self._car = car
        self._model = model
        self._max_speed = max_speed

    def __str__(self):
        return "{} {} with maximum speed {} kmph.".format(self._car, self._model, self._max_speed)

    def __repr__(self):
        return self.__str__()
