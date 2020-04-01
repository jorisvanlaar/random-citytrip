"""Joris van laar - Python (PTH) - 20-01-2020"""
from Vehicle import Vehicle


class Car(Vehicle):
    in_stock = 10

    @classmethod
    def add_to_reservation(cls):
        if Car.in_stock > 0:
            return Car()
        else:
            print("We don't have a car available, our apologies.")

    def __init__(self):
        super().__init__(vtype='car', km_cost=2)
        Car.in_stock -= 1
        if Car.in_stock < 0:
            Car.in_stock = 0

    def __repr__(self):
        return f"Vehicle type: {self._vtype}"

    def drive(self):
        print(f"This vehicle can move on land")


