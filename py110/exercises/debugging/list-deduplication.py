data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
for i in data:
    if i not in unique_data:
        unique_data.append(i)

print(unique_data == [4, 2, 1, 3]) # order not guaranteed

# order can be preserved by using an empty list to add items that are not in that list
