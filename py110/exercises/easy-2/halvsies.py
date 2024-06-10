def halvsies(lst):
    half = (len(lst)/2).__ceil__()
    r_lst = [lst[0:half], lst[half::]]
    return r_lst



# All of these examples should print True

print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
