def is_balanced(string):
    balanced = False
    if string.count('(') == string.count(')'):
        if string.count('(') == 0:
            balanced = True
        for segment in string.split(")"):
            if "(" in segment and string.rfind('(') < string.rfind(')'):
                balanced = True
    return balanced
                
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
