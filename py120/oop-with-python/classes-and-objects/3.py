"""
Add a method to the Car class that lets you spray paint the car a specific color. 
Don't use a setter method for this. 
Instead, create a method whose name accurately describes what it does. 
Don't forget to test your code.
"""

class Car:

    @classmethod
    def calculate_mileage(cls, gallons, miles):
        mileage = miles / gallons
        print(f"Your mileage is {mileage}.")

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
    def color(self, new_color):
        self._color = new_color

    def spray_paint(self, spray_color):
        self.color = spray_color
        print(f"Your color is now {self.color}")

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
toyota.spray_paint('pink')
toyota.spray_paint('red')

toyota.calculate_mileage(15, 500)
