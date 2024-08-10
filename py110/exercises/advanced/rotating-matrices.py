def rotate90(m):
    l = []
    res = []
    length = len(m[0])
    count = 0
    if m:

        for i in range(len(m)):
            print(i, 'i')
            count = 0
            #for j in range(len(m)):
            for j in range(len(m[i])):
                print(j, 'j', m[i][j])
                #l.append(m[j][i])
                print(m[i], 'mi')

            res += [l[::-1]]
            l = []
    print(res)
    return res




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
