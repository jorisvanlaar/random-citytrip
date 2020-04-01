"""Joris van laar - Python (PTH) - 20-01-2020"""


class Vehicle:
    @classmethod
    def add_to_reservation(cls):
        raise NotImplementedError("Subclass of Vehicle needs to implement this method")

    def __init__(self, vtype, km_cost):
        self._vtype = vtype
        self._km_cost = km_cost

    def __repr__(self):
        return f"Vehicle type: {self._vtype}, costs {self._km_cost} euro p/km"

    @property
    def vtype(self):
        return self._vtype

    @vtype.setter
    def vtype(self, new_vtype):
        self._vtype = new_vtype

    @property
    def km_cost(self):
        return self._km_cost

    @km_cost.setter
    def km_cost(self, new_km_cost):
        self._km_cost = new_km_cost

