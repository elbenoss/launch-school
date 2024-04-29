#Assume you have the following sequences:

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

#Write some code that combines the sequences into a list of tuples. Each tuple should contain one member of each sequence. Print the final result so you can see all the values, which should look like this:

new_list = []
for i in range(0, len(my_str)):
	new_tuple = (my_str[i], my_list[i], my_tuple[i], my_range[i])
	new_list.append(new_tuple)
print(new_list)
