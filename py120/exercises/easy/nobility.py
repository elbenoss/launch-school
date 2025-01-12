class WalkMixin:
    def walk(self):
        return f"{self} {self.gait()} forward"


class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Person(Animal, WalkMixin):
    def gait(self):
        return 'strolls'

class Cat(Animal, WalkMixin):
    def gait(self):
        return 'saunters'

class Cheetah(Cat):
    def gait(self):
        return 'runs'


class Noble(Person):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __str__(self):
        return f"{self.title} {self.name}"
    
    def gait(self):
        return 'struts'




byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"


