"""
1.
Sort the following list of numbers first in ascending numeric order, then in descending numeric order. Do not mutate the list.
"""
lst = [10, 9, -6, 11, 7, -16, 50, 8]

sorted(lst)
[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
sorted(lst, reverse=True)
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort

"""
2. 
Repeat the previous exercise but, this time, perform the sort by mutating the original list.
"""
lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort()
[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort

lst.sort(reverse=True)
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort


"""
3.
Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.
"""
lst = [10, 9, -6, 11, 7, -16, 50, 8]

[-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
lst.sort(key=str)

[9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort
lst.sort(key=str, reverse=True)


"""
4.
How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?
"""

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def years(lst):
    t, a, p = lst
    print(lst.get(p))
    return int(lst.get(p))

books.sort(key=years)
