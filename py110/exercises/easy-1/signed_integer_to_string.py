def signed_integer_to_string(integer):
    str_int_dict = {
        1: '1', 
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        0: '0',
    } 
    return_str = ''
    if integer > 0:
        sign = "+"
    elif integer < 0:
        sign = "-"
    integer = abs(integer)
    if integer < 9:
        return str_int_dict.get(integer)
    while integer > 9:
        integer, place = divmod(integer, 10)
        return_str += str_int_dict.get(place) 
    return_str += str_int_dict.get(integer)
    return_str += sign
    return return_str[::-1]




print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
