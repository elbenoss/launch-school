def unique_from_first(lst1, lst2):
    return {i for i in lst1 if i not in lst2}

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})
