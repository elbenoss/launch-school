# Write the code needed to make the following code work as shown:

class Vehicle:

    amount = 0

    def __init__(self):
        Vehicle.amount += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.amount

class Car(Vehicle):
    def __init__(self):
        super().__init__()


class Truck(Vehicle):
    def __init__(self):
        super().__init__()


class Boat(Vehicle):
    def __init__(self):
        super().__init__()


print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8
