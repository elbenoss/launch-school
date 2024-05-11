# Write a function that takes a short line of text and prints it within a box.

def print_in_box(text):
    length = len(text) + 2
    print("+" + "-"*length + "+") 
    print("|" + " "*length + "|")
    print("|" + " " +  text + " " + "|")
    print("|" + " "*length + "|")
    print("+" + "-"*length + "+") 

print_in_box('To boldly go where no one has gone before.')

# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

print_in_box('')

# +--+
# |  |
# |  |
# |  |
# +--+

# print(len(""))