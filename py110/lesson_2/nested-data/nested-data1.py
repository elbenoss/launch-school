""""
1. 
For each object shown below, demonstrate how you would access the letter g.
"""

lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

lst1[2][1][3]

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

lst2[1]['third'][0]


lst3 = [['abc'], ['def'], {'third': ['ghi']}]

lst3[2]['third'][0][0]


dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

dict1['b'][1]


# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

list(dict2['3rd'].keys())[0]