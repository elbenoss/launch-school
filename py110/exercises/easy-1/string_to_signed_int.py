def string_to_integer(s):
    DIGITS = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
    }
    value = 0
    for char in s:
        value = (10 * value) + DIGITS[char]
    return value

def string_to_signed_integer(str):
    
    if '-' in str:
        str = str.replace('-', '')
        return -string_to_integer(str)
    elif '+' in str:
        str = str.replace('+', '')
    return string_to_integer(str)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
