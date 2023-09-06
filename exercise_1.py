"""
Exercise #1

Filter out all of the empty strings from the list below

Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
"""


places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

empty_place = list(filter(lambda p: p.strip() != "", places))

print(empty_place)
