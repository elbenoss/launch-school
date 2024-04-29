#Write a function that returns the first element of a list provided as an argument. For example:

def first(list):
    try:
        return list[0]
    except:
        return 'No elements in list'

print(first(['Earth', 'Moon', 'Mars']))  # Earth
