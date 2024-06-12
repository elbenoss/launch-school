def substrings(string):
    res = []
    for i in range(len(string)):
        for j in range(len(string)):
            res += string[i:j + 1].split()
    return res



expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
