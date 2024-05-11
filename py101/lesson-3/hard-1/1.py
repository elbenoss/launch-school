# Will the following functions return the same results?
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# the second functions doesn't return the dictionary
# the return is processed before the braces in the second function making the code unreachable