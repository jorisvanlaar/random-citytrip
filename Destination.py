"""Joris van laar - Python (PTH) - 20-01-2020"""


class Destination:
    def __init__(self, city, distance):
        self._city = city
        self._distance = distance

    def __repr__(self):
        return f"Destination: {self._city}, {self._distance}km from A'dam"

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        self._city = new_city

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, new_distance):
        self._distance = new_distance



