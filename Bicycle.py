"""Joris van laar - Python (PTH) - 20-01-2020"""
from Vehicle import Vehicle


class Bicycle(Vehicle):
    in_stock = 10

    @classmethod
    def add_to_reservation(cls):
        if Bicycle.in_stock > 0:
            return Bicycle()
        else:
            print("We don't have a bicycle available, our apologies.")

    def __init__(self):
        super().__init__(vtype='bicycle', km_cost=1)
        Bicycle.in_stock -= 1
        if Bicycle.in_stock < 0:
            Bicycle.in_stock = 0

    def __repr__(self):
        return f"Vehicle type: {self._vtype}"

    def cycle(self):
        print(f"This vehicle can move on land")





