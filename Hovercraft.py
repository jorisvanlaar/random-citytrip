"""Joris van laar - Python (PTH) - 20-01-2020"""
from Car import Car
from Boat import Boat


class Hovercraft(Car, Boat):
    in_stock = 1

    @classmethod
    def add_to_reservation(cls):
        if Hovercraft.in_stock > 0:
            return Hovercraft()
        else:
            print("We don't have a hovercraft available, our apologies.")

    def __init__(self, vtype='hovercraft', km_cost=8):
        self._vtype = vtype
        self._km_cost = km_cost
        Hovercraft.in_stock -= 1
        if Hovercraft.in_stock < 0:
            Hovercraft.in_stock = 0

    def __repr__(self):
        return f"Vehicle type: {self._vtype}"

