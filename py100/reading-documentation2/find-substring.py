#Using the official Python documentation, can you determine how to check whether a string contains a specific substring?
# .find returns index if found or -1 if the substring is not found
# .index returns index if found or ValueError when substring is not found
# str in str returns true when substring is found false otherwise
string = 'testing for substring'

print(string.find('est'))
print(string.index('for'))
print("dubstring" in string)