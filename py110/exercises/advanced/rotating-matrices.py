def rotate90(m):
    res = []

    for i in range(len(m[0]) - 1, -1, -1):
        temp = []
        for j in range(len(m)):
            temp.append(m[j][i])
        res.insert(0, temp[::-1])
    return res


"""
input: list containing sub-lists
output: values from sublists reorganized on 
    * starting from last list
    * starting from first element
    ex. 3 items 3 sublists
    2[0], 1[0], 0[0]
    then
    2[1], 1[1], 0[1]
"""



matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
