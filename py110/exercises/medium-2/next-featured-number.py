"""
A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits occurring exactly once each. For example, 49 is a featured number,
but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

NOTE: The largest possible featured number is 9876543201.

"""

memo = [7]

def is_featured(number):
    """   
    featured = [i*7 for i in range(100_000_000) if i*7 % 2 != 0 and len(set(str(i*7))) == len(str(i*7))]

    """



    print(memo[-1])

    for i in range(memo.index(memo[-1]), number):
        if i*7 % 2 != 0 and len(set(str(i*7))) == len(str(i*7)) and i * 7 > number:
            memo.append(i*7)
            print(i * 7)
            return i * 7
        elif number >= 9876543201:
            return "There is no possible number that fulfills those requirements."


    """
    feat = [j for j in featured if j > number]
    if feat and number < 9876543201:
        print(feat)
        return feat[0]
    else:
        return "There is no possible number that fulfills those requirements."
    """

print(is_featured(12) == 21)                  # True
print(is_featured(20) == 21)                  # True
print(is_featured(21) == 35)                  # True
print(is_featured(997) == 1029)               # True
print(is_featured(1029) == 1043)              # True
print(is_featured(999999) == 1023547)         # True
print(is_featured(999999987) == 1023456987)   # True
print(is_featured(9876543186) == 9876543201)  # True
print(is_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(is_featured(9876543201) == error)       # True
