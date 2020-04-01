"""Joris van laar - Python (PTH) - 20-01-2020"""
from Vehicle import Vehicle


class Boat(Vehicle):
    in_stock = 50

    @classmethod
    def add_to_reservation(cls):
        if Boat.in_stock > 0:
            return Boat()
        else:
            print("We don't have a boat available, our apologies.")

    def __init__(self):
        super().__init__(vtype='boat', km_cost=5)
        Boat.in_stock -= 1
        if Boat.in_stock < 0:
            Boat.in_stock = 0

    def __repr__(self):
        return f"Vehicle type: {self._vtype}"

    def sail(self):
        print(f"This vehicle can move on water")

