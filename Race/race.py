from driver import Driver
from car import Car
class Race:
    def __init__(self, drivers, crash_chance):
        self._drivers = drivers
        self._crash_chance = crash_chance
