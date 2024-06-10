def interleave(lst1, lst2):
    r_lst = []
    for i in range(len(lst1)):
        r_lst.append(lst1[i])
        r_lst.append(lst2[i])
    return r_lst

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
