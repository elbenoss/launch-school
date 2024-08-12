"""
Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.
"""
import copy

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
ans = [[], [3, 12], [9], [15, 18]]



res = copy.deepcopy(lst)

for i in range(len(lst)):
    for j in lst[i]:
        if j % 3 != 0:
            res[i].remove(j)

print(res)
print(res == ans)
