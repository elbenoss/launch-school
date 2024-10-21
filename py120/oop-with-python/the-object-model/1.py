"""
How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.

What class you create doesn't matter, provided it satisfies the above requirements.
"""

class Germanic:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

gepid = Germanic("Gepid")
geat = Germanic("Geat")
