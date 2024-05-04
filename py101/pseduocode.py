# get list of strings
# perform join on list
# print result

# list = ['a stromg', 'p[c', 'a pocke', 'or two']


# out = "".join(list)
# print(out)

# string  = 'an greattt example strings g'
# c = 'g'

# def third_char(string, c):
#     count = 0
#     for i in range(len(string)):
#         if string[i] == c:
#             count += 1
#         if count == 3:
#             print(i)
#             break
#     if count < 3:
#         print(None)

# third_char(string, c)



def merge(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i])
        new_list.append(list2[i])
    print(new_list)
merge([1, 2, 3], [4, 5, 6])