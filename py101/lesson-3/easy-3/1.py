# Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]

del numbers[0:4]

for _ in range(len(numbers)):
   numbers.pop()

numbers.clear()

while numbers:
    numbers.pop()
