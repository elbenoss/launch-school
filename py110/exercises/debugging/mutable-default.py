def append_to_list(value):
    lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

# 1 is already added to lst for second function call, needs mutable lst removed
