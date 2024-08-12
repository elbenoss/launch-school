"""
Given the following data structure, return a new list with the same structure, but with the values in each sublist ordered in ascending order. 
Use a comprehension if you can. (Try using a for loop first.)
"""

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_lst = []
for l in lst:
    l.sort()
    new_lst.append(l)
print(new_lst)


new_lst2 = [sorted(l) for l in lst]
print(new_lst2)
print(new_lst2 == [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']])


# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
