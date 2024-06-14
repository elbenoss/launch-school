def unique_sequence(lst):
    length = len(lst)
    while max([lst.count(i) for i in lst]) > 1:
        for j in range(length):
            if j >= length:
                j = 0
            if lst[j] == lst[j - 1]:
                lst.pop(j)
                length -= 1
    return lst

original = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6]
expected = [1, 2, 3, 4, 5, 6]
print(unique_sequence(original) == expected)      # True

