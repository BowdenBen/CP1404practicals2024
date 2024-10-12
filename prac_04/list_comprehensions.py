"""
CP1404/CP5632 Practical
List comprehensions
"""
from prac_03.string_formatting import number

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# this splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# this example uses filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# and here's the join string method being used to create a single string from the names like:
# 'Ada Alan Angel Bob Jimi'
print(" ".join(sorted(names)))

# The list comprehension iterates over each full name in the list `full_names`
# For each full name, the `lower()` method is called to convert the name to lowercase.
# The result is stored in the list `lowercase_full_names`.
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

# This list comprehension converts each string in `almost_numbers` to an integer using `int()`.
# The result is stored in the list `numbers`.
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(number) for number in almost_numbers]
print(numbers)

# After converting to integers, this list comprehension filters the numbers by checking if they are greater than 9.
# Only numbers that satisfy the condition `number > 9` are included in the resulting list.
numbers_greater_than_9 = [number for number in numbers if number > 9]
print(numbers_greater_than_9)

# The list comprehension iterates through `full_names`, splits each name into first and last names using `split()`.
# It then checks if the full name length is greater than 11 characters.
# If true, it takes the last name (index 1 of the split result).
# Finally, `join()` combines the selected last names into a single string, separated by commas.
long_last_name = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print(long_last_name)
# the result should be: 'Harlem, Hendrix, Lovelace'