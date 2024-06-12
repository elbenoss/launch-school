def leading_substrings(string):
    res = []
    for i in range(len(string) + 1):
        res += string[0:i].split()
    return res

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzz'])
