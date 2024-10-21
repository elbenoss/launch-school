"""
Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car. 
You should also add getter methods that let you view but not modify the car's model and year. 
Don't forget to write some tests.
"""

class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color
        
    @color.setter
    def set_color(self, new_color):
        self._color = new_color

    def engine_on(self):
        print('The engined has turned on.')

    def engine_off(self):
        self._speed = 0
        print('The engine has turned off.')

    def accelerate(self, number):
        self._speed += number
        print(f'Accelerating to {self._speed} mph')

    def brake(self, number):
        self._speed = number
        print(f'Slowing to {self._speed} mph')

    def current_speed(self):
        print(f'Your current speed is {self._speed} mph')


toyota = Car('Camry', 2020, 'white')

print(toyota.model)
print(toyota.year)
print(toyota.color)

toyota.set_color = 'orange'

print(toyota.color)


