import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)
original[0][0] = 99
print(copied[0] == [1])

# copy.copy returns a shallow copy, where the nested values are references
# copy.deepcopy will copy the nested values
