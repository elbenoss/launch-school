class Person:

    def __init__(self, name):
        self._name = name
        self._first_name = name
        self._last_name = ''

    def __str__(self):
        return self.name


    @property
    def name(self):
        return self._first_name + ' ' + self._last_name
    @name.setter

    def name(self, new_name):
        self._name = new_name
        new_names = new_name.split(" ")
        if len(new_names) > 1:
            self.first_name = new_names[0]
            self.last_name = new_names[1]
        else:
            self.first_name = new_name[0::]
            self.last_name = '' 

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
        #self._name += first_name
    

    @property 
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name




# 1
'''
bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert
'''


# 2
"""
bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith
"""

# 3
"""
bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams
"""

# 4
bob = Person('Robert Smith')
rob = Person('Robert Smith')

print(bob.name == rob.name)
print(bob == rob)
