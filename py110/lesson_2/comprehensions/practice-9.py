"""
This problem may prove challenging. Try it, but don't stress about it. If you don't solve it in 20 minutes, you can look at the answer.

Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.
"""

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

ans = [{'e': [8], 'f': [6, 10]}]


res = []
check = []
for dic in lst:
    count = 0
    for key, value in dic.items():
        for number in value:
            if number % 2 != 0:
                count += 1
    if count == 0:
        res.append(dic)
print(res)


def is_even(d):
    b = True
    for v in d.values():
        if not all([n % 2 == 0 for n in v]):
            b = False
    return b

comp = [d for d in lst if is_even(d)]
print(comp)


print(res == comp == ans)
# [{e: [8], f: [6, 10]}]
