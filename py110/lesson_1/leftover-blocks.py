"""
Make notes of your mental model for the problem, including:
inputs and outputs.
explicit and implicit rules.
Write a list of clarifying questions for anything that isn't clear.

- Step 1
input: integer (num of blocks)
output: integer (num of blocks leftover from tallest possible structure)
rules:
    1. top-layer is 1 block
    2. upper layer supported by 4 blocks in lower
    3. no gaps between blocks
questions:
    1. can 1/4 exists as simplest possible structure?
    2. is 4 blocks only on bottom layers
-
- Step 2
1. 2 blocks reesults in 1 leftover so probably top = 1
2. test case 5 has 0 leftovers. possibly 1 and 4
3. 14 have 0 leftover so 
    1,2,3,4,5 = 15
    1,4,4,5 = 14
    1,2,3,4 = 10
    1,2,3,4,5 = 15
-
- Step 3
list to organize length easily
-
- Step 4
given n
if n >= 1
then 1 top block is given
if n > 5= for every four blocks passed 1 add a layer of 4 blocks
-
- Step 5
"""



def calculate_leftover_blocks(n):
    lst = [i ** 2 for i in range(0, int(n ** .5) + 1)]
    if n == sum(lst):
        return 0
    elif sum(lst) > n:
        return n - sum(lst[0:len(lst)-1])
    else:
        return abs(n - sum(lst))


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
