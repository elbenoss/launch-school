# Going back to your solution to exercise 1, refactor the code to replace any methods that can be converted to static methods. 
# Once you have done that, ask yourself whether the conversion to a static method makes sense.


class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0

    @staticmethod
    def calculate_mileage(miles, gallons):
        mileage = miles / gallons
        print(f"Your mileage is {mileage}.")

    @staticmethod
    def engine_on():
        print('The engined has turned on.')

    @staticmethod
    def engine_off():
        #self._speed = 0
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

Car.engine_on()
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
Car.engine_off()
Car.calculate_mileage(500, 15)

"""
only engine_on, and engine_off without the speed change can be converted to a staticmethod
in this particular case, engine_on isn't a requirement of acceleration nor engine_off and isn't 
relevant to instance variables, this is true of engine_off without the speed change
mileage method can be converted to static because it only requires inputs neither related to the class or instance
"""
