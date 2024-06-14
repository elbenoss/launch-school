def sum_digits(integer):
    summation = 0
    while integer > 9:
        summation += integer % 10
        integer //= 10
    summation += integer
    return summation


print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True
