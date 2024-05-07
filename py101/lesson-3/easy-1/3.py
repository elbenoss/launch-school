# Starting with the string:
famous_words = "seven years ago..."
# Show two different ways to create a new string with "Four score and " prepended to the front of the string.
new_string = "Four score and " + famous_words
print(new_string)
new_string = f"Four score and {famous_words}"
print(new_string)
new_string = "Four score and "
new_string += famous_words
print(new_string)
