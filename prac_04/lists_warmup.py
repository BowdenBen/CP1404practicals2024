
numbers = [3, 1, 4, 1, 5, 9, 2]

"""
1. numbers[0]        --> 3
2. numbers[-1]       --> 2 (last element)
3. numbers[3]        --> 1 (4th element)
4. numbers[:-1]      --> [3, 1, 4, 1, 5, 9] (all elements except the last one)
5. numbers[3:4]      --> [1] (slice from index 3 up to (but not including) index 4)
6. 5 in numbers      --> True (5 is in the list)
7. 7 in numbers      --> False (7 is not in the list)
8. "3" in numbers    --> False (string "3" is not in the list, only integers)
9. numbers + [6, 5, 3] --> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] (concatenation of two lists)
"""

# Change the first element to "ten"
numbers[0] = "ten"
print(numbers)

# Change the last element to 1
numbers[-1] = 1

# Print all elements except the first two
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
