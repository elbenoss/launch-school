def multiply_list(lst1, lst2):
    r_lst = []
    for i in range(len(lst1)):
        r_lst.append(lst1[i] * (lst2[i]))
    return r_lst




list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
