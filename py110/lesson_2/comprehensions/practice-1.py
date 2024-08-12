"""
Consider the following nested dictionary:
"""

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total = 0
for att in munsters.values():
    if att['gender'] == 'male':
        total += (att['age'])
print(total)


print(sum([att['age'] for att in munsters.values() if att['gender'] == 'male']) == 444)


"""
Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.
The result should be 444.
"""
