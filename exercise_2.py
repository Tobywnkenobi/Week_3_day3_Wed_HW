"""
Exercise #2

Write an anonymous function that sorts this list by the last name...
Hint: Use the ".sort()" method and access the key"

Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

"""

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

def author_names(lst_nm):
    return lst_nm.split()[-1].lower()

last_full_list = [(author_names(lst_nm), author) for lst_nm in author]

last_full_list.sort()

author_sort = [n[1] for n in last_full_list ]
print(author_sort)

