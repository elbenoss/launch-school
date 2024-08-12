"""
Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables. 
The sizes should be uppercase, and the colors should be capitalized.
"""

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

list1 = [[word.title() for word in dict1[key].get('colors')] if dict1[key].get('type') == 'fruit' else dict1[key].get('size').upper() for key in dict1.keys()]

print(list1 == [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"])


# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
