#Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.
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
