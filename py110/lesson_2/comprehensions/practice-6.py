"""
Given the following data structure, return a new list identical in structure to the original but, 
with each number incremented by 1. Do not modify the original data structure. Use a comprehension.
"""

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]


# res = {let: num + 1 for dic in lst for let, num in dic.items()}
res2 = []
for i in range(1, len(lst) + 1):
    dic = dict(lst[i-1])
    l_dic = list(lst[i-1])
    res2.append(dict(lst[i-1]))
    for j in range(len(l_dic)):
        res2[i-1][l_dic[j]] += 1

#res3 = [{list(lst[i-1])[j]:lst[i-1].get(list(lst[i-1])[j]) + 1} for i in range(1, len(lst) + 1) for j in range(len(lst[i-1]))]

res4 = [{list(lst[i-1])[j]:lst[i-1].get(list(lst[i-1])[j]) + 1 for j in range(len(lst[i-1]))} for i in range(1, len(lst) + 1)]
ans = [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]


print(res4 == ans)
