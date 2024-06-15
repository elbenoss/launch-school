data_set = {1, 2, 3, 4, 5}
for item in data_set.copy():
    if item % 2 == 0:
        data_set.remove(item)

# alternate       
print({item for item in data_set if item % 2 != 0})


# items 2 and 4 are removed shrinking the data_set from 5 to 3, causing the runtime error
# a copy of the set can be used as reference instead of the set being mutated
