# Using the following string, print a string that contains the same value,
# but using all lowercase letters except for the first character, which should be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
print(munsters_description[0:2].title() + munsters_description[2:].lower())
# => 'The munsters are creepy and spooky.'
list = [letter for letter in munsters_description.lower().split()]
list[0] = list[0].title()
print(" ".join(list))
