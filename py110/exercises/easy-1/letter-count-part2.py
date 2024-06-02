def word_sizes(str):
    counts = []
    c_dict = {}

    if str:
        list = str.split()

        for word in list:
            for char in word:
                if not char.isalpha():
                    word = word.replace(char, "")
            counts.append(len(word))

        for i in counts:
            c_dict[i] = counts.count(i)
    return c_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
