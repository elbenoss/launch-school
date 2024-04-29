#Use a for loop to iterate over the numbers dictionary and return a list containing each number divided by 2 as an integer. 
#If a number is odd, the result should be truncated to an integer. Assign the returned list to a variable named half_numbers and print its value using print.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
# [50, 25, 12]

half_numbers = []
# for number in numbers:
#     half_numbers.append((numbers[number])//2)
for value in numbers.values():
    half_numbers.append(value // 2)
print(half_numbers)
