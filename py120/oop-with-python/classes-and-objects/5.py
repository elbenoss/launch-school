# Create a Person class with two instance variables to hold a person's first and last names. 
# The names should be passed to the constructor as arguments and stored separately. 
# The first and last names are required and must consist entirely of alphabetic characters.


class Person:

    def __init__(self, first, last):
        self._set_name(first, last)

        #self._forename = first
        #self._surname = last
        #if (all([True if letter.isalpha() else False for letter in first])) and (all([True if letter.isalpha() else False for letter in last])):
        #    pass
        #else:
        #    raise ValueError('Name must be alphabetic.')
    
    @property
    def name(self):
        return self._forename.capitalize() + ' ' + self._surname.capitalize()

    @name.setter
    def name(self, name):
        self._forename, self._surname = name[0], name[1]

    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError('Name must be alphabetic.')

    def _set_name(self, first, last):
        Person._validate(first)
        Person._validate(last)
        self._forename = first
        self._surname = last



actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.
