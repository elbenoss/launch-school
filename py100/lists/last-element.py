#Write a function that returns the last element of a list provided as an argument. For example:

def last(list):
    try:
        return list[-1]
    except:
        return 'No elements to return'

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))