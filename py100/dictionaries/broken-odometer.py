#Using the following code, delete the 'mileage' key and its associated value from car.

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}
print(car)
# car.__delitem__('mileage')
del car["mileage"]
print(car)