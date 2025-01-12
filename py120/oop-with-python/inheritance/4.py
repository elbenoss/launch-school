import pprint
# Print the method resolution order for cars, trucks, boats, and vehicles as defined in the previous exercise.

class Vehicle:
    amount = 0

    def __init__(self):
        Vehicle.amount += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.amount

class SignalMixin:

    def signal_left(self):
        print("Signalling left")

    def signal_right(self):
        print("Signalling right")

    def signal_off(self):
        print("Signal is now off")


class Car(SignalMixin, Vehicle):
    
    def __init__(self):
        super().__init__()

class Truck(SignalMixin, Vehicle):

    def __init__(self):
        super().__init__()

class Boat(Vehicle):

    def __init__(self):
        super().__init__()


pprint.pp(Car.mro())
print()
pprint.pp(Truck.mro())
print()
pprint.pp(Boat.mro())
print()
pprint.pp(Vehicle.mro())
