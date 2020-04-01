"""Joris van laar - Python (PTH) - 20-01-2020"""


class Reservation:
    def __init__(self, customer, city, distance, vehicle, price):
        self._customer = customer
        self._city = city
        self._distance = distance
        self._vehicle = vehicle
        self._price = price

    def __repr__(self):
        return f"Reservation by {self._customer} to {self._city} with a {self._vehicle}"

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, new_customer):
        self._customer = new_customer

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

    @property
    def vehicle(self):
        return self._vehicle

    @vehicle.setter
    def vehicle(self, new_vehicle):
        self._vehicle = new_vehicle

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price
















