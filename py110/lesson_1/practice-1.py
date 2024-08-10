
# fruits = ("apple", "banana", "cherry", "date", "banana")


"""
How would you count the number of occurrences of "banana" in the tuple?
"""
# fruits.count("banana")



# numbers = {1, 2, 3, 4, 5, 5, 4, 3}
# print(len(numbers)) # 5
"""
What is the set's length? Try to answer without running the code.
"""



# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
"""
How would you obtain a set that contains all the unique values from both sets?
"""
# a !|= b




# Given the following code, what would the output be? Try to answer without running the code.
"""
names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions) # {"Fred": 0, "Barney": 1, "Wilma": 2, "Betty": 3, "Pebbles": 4, "Bambam": 5}
"""


"""
# Calculate the total age given the following dictionary:
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

total_age = sum([int(age) for age in ages.values()])
minimum_age = min(ages.values())
print(minimum_age)
"""

"""
# What would the following code output? Try to answer without running the code.
words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words) # ['bear']
"""

"""
# Given the following string, create a dictionary that represents the frequency with which each letter occurs. 
# The frequency count should be case-sensitive:
statement = "The Flintstones Rock"
# The output should resemble the following:
# Pretty printed for clarity
{
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}
lst = [(let, statement.count(let)) for let in statement]
print(dict(lst))
"""



# What is the return value of the list comprehension below? Try to answer without running the code.
[num for num in [1, 2, 3] if num > 1] # [2, 3]


# What does the following code print and why?
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem()) # ('b', 'bear')


# What does the following code return? Try to answer without running the code.
lst = [1, 2, 3, 4, 5]
lst[:2] # [1, 2]


# What would be the output of the below code? Try to answer without running the code.
frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6) # error?
print(frozen) # {1, 2, 3, 4, 5}




