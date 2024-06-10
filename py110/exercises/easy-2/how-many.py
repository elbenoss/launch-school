def count_occurrences(lst):
    r_lst = []
    for item in lst:
        if item not in r_lst:
            r_lst.append(item)
            item_str = (' => ' + str(lst.count(item)))
            r_lst.append(item_str)
    for i in range(1, len(r_lst), 2):
        print(''.join(r_lst[i-1] + r_lst[i]))




vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
