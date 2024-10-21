"""
Create a Car class that meets these requirements:

    Each Car object should have a model, model year, and color provided at instantiation time.
    You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.

    Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.

    Create a method that prints a message about the car's current speed.
    Write some code to test the methods.

"""

class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0

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
honda = Car('Accord', 1990, 'orange')
oldsmobile = Car('Cutlass', 1979, 'brown')
ford = Car('Escort', 1982, 'yellow')

toyota.engine_on()
toyota.accelerate(5)
toyota.accelerate(20)
toyota.accelerate(30)
toyota.current_speed()
toyota.brake(50)
toyota.current_speed()
toyota.accelerate(10)
toyota.brake(15)
toyota.brake(30)
toyota.current_speed()
toyota.engine_off()
