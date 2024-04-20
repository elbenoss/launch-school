7# 1
"""
counter doesn't increment in loop
"""
# 3
#my_list = [6, 3, 0, 11, 20, 4, 17]
#i = 0
#while i < len(my_list):
#    print(my_list[i])
#    i += 1
#for num in my_list:
#   print(num)
# 4
#my_list = [6, 3, 0, 11, 20, 4, 17]
#i = 0
#while i < len(my_list):
#    if my_list[i]%2==0:
#        print(my_list[i])
#    i += 1
#for num in my_list:
#    if num%2!=0:
#        print(num)
# 5
#my_list = [
#    [1, 3, 6, 11],
#    [4, 2, 4],
#    [9, 17, 16, 0],
#]
#for nests in my_list:
#    for nest in nests:
#        if nest%2==0:
#            print(nest)
# 6
#my_list = [
#    1, 3, 6, 11,
#    4, 2, 4, 9,
#    17, 16, 0,
#]
#new_list = ['even' if num%2==0 else 'odd' for num in my_list]
#print(new_list)
# 7
#my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#            -4, None, {1, 2, 3}, False)
#def find_integers(tuple):
#    list = []
#    for item in tuple:
#        if type(item) is int:
#            list.append(item)
#    return list
#integers = find_integers(my_tuple)
#print(integers)
# 8
'''my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}
new_dict = {name: len(name) for name in my_set if len(name)%2!=0}
print(new_dict)'''
#9
#def factorial(n):
#    i = 0
#    fac = 1
#    while i < n:
7#        i += 1
#        fac *= i
#    print(fac)
#factorial(8)





#10
'''import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number >= highest:
        break
'''


#11
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

i = 0
while i < len(my_list):
    i2 = 0
    while i2 < len(my_list[i]):
        if my_list[i][i2] % 2 == 0:
            print(my_list[i][i2])
        i2 += 1
    i += 1
