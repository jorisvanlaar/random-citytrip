"""Joris van laar - Python (PTH) - 20-01-2020"""
from Vehicle import Vehicle


class Train(Vehicle):
    in_stock = 30

    @classmethod
    def add_to_reservation(cls):
        if Train.in_stock > 0:
            return Train()
        else:
            print("We don't have a train available, our apologies.")

    def __init__(self):
        super().__init__(vtype='train', km_cost=4)
        Train.in_stock -= 1
        if Train.in_stock < 0:
            Train.in_stock = 0

    def __repr__(self):
        return f"Vehicle type: {self._vtype}"

    def ride(self):
        print(f"This vehicle can move on land")

