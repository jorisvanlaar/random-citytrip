"""Joris van laar - Python (PTH) - 20-01-2020"""
from Vehicle import Vehicle


class Airplane(Vehicle):
    in_stock = 20

    @classmethod
    def add_to_reservation(cls):
        if Airplane.in_stock > 0:
            return Airplane()
        else:
            print("We don't have an airplane available, our apologies.")

    def __init__(self):
        super().__init__(vtype='airplane', km_cost=3)
        Airplane.in_stock -= 1
        if Airplane.in_stock < 0:
            Airplane.in_stock = 0

    def __repr__(self):
        return f"Vehicle type: {self._vtype}"

    def fly(self):
        print(f"This vehicle can move in the air")

