# Add a class method to your Car class that calculates and prints any car's average gas mileage (miles per gallon). 
# You can compute the mileage by dividing the distance traveled (in miles) by the fuel burned (in gallons).


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

    def calculate_mileage(self, miles, gallons):
        mileage = miles / gallons
        print(f"Your mileage is {mileage}.")

toyota = Car('Camry', 2020, 'white')

toyota.engine_on()
toyota.accelerate(60)
toyota.brake(0)
toyota.engine_off()
toyota.calculate_mileage(500, 15)

