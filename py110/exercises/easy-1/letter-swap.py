def swap(str):
    new_lst = []
    for word in str.split():
        if len(word) > 1:
            new_lst.append(word[-1] + word[1:len(word)-1:] + word[0])
        else:
            new_lst.append(word)

    return ' '.join(new_lst)



print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

