# Using the code below, determine the method resolution order (MRO) when accessing cat1.color. 
# Only list the classes and mix-ins Python will check when searching for the color method. 
# Do not use the mro method.

class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()
cat1.color


"""
cat1 belongs to the Cat class
Cat class does not define color
Cat class is a subclass of Animal
Animal does not define color
Animal belongs to object class
Object base class does define color
Class sets to None with attribute error
"""

# Cat
# Animal
# object
# None -> Attribute Error

