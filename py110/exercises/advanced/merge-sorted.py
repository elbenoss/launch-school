"""
Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in ascending sorted order. 
You may assume that the lists contain either all integer values or all string values.

You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.
"""

def merge(lst1, lst2):
    res = lst1 + lst2
    for i in range(1, len(res)):
        for j in range(1, len(res)):
            if res[j -1] > res[j]:
                res[j - 1], res[j] = res[j], res[j - 1]
    return res


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)
