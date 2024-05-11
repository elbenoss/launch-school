# What will the following code output?
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

# my_list2 is a shallow copy of my_list1
# this creates a different location for the outer elements of the list
# however, it references the same location in memory for the nested elements within the list
# the first key value is ressasigned to 42
# my_list1 prints the dictionary with the reassignment
