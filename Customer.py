"""Joris van laar - Python (PTH) - 20-01-2020"""


class Customer:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return f"Customer name: {self._name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

