def alphabetic_number_sort(lst, res):
    eng_sort = {
            8: 1,
            18: 2,
            11: 3,
            15: 4,
            5: 5,
            4: 6,
            14: 7,
            9: 8,
            19: 9,
            1: 10,
            7: 11,
            17: 12,
            6: 13,
            16: 14,
            10: 15,
            13: 16,
            3: 17,
            12: 18,
            2: 19,
            0: 20,
            }
    return sorted(lst, key=eng_sort.get) == res


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list, expected_result))
# Prints True
