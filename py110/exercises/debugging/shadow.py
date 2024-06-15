def sumf(numbers, factor):

    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sumf(numbers, 2) == 20)

# sum is in-built function shadowed by the defined function
# fix by chaning function name
