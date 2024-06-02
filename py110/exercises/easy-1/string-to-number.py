def string_to_integer(str):
    sum = 0
    for i in range(len(str)):
        num = 10 ** str.index(str[-1-i]) 
        match str[i]:
            case '1':
                sum += num * 1
            case '2':
                sum += num * 2
            case '3':
                sum += num * 3
            case '4':
                sum += num * 4
            case '5': 
                sum += num * 5
            case '6': 
                sum += num * 6
            case '7': 
                sum += num * 7
            case '8':
                sum += num * 8
            case '9':
                sum += num * 9
    return sum


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
