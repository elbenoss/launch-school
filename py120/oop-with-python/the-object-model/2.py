"""
Given an instance of a Foo object, show two ways to print I am a Foo object without hardcoding the word Foo.
"""

class Foo:

    def __init__(self):
        type_name = type(self).__name__
        print(f"I am a {type_name} object")
    def print_class(self):
        print(f"I am a {self.__class__.__name__} object")

instance = Foo()
instance.print_class()
