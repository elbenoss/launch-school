def  running_total(lst):
    total = 0
    new_lst = []
    for i in range(len(lst)):
        total += lst[i]
        new_lst.append(total)
    return new_lst

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
