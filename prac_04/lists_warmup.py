
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


# """
# The following are practice examples from this weeks lectures
# """
# # Initial score list
# score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
#
# # Ask the user for a new name and score
# new_entry = input("Enter a new name and score (format: name score): ")
#
# # Split the input into name and score
# name, score = new_entry.split()
# score = int(score)  # Convert score to an integer
#
# # Add the new entry to the list
# score_pairs.append([name, score])
#
# """
# Sort the list by scores in descending order
# lambda x: Defines an anonymous function that takes one argument, x. Each element of the list score_pairs will be
# passed to this function one by one. In this case, each element is a list (like ['Derek', 7]).
# x[1]: This part of the lambda function tells Python to use the second element of the list (the score) for
# sorting. x[1] means "the second item in x", where x is one of the [name, score] pairs.
# For example, when x = ['Derek', 7], x[1] will be 7.
# """
# sorted_scores = sorted(score_pairs, key=lambda x: x[1], reverse=True)
#
# # Display the final sorted list
# print("Final scores sorted from highest to lowest:")
# for pair in sorted_scores:
#     print(f"{pair[0]}: {pair[1]}")
#
# # Define a string variable called 'text'
# text = "This is a sentence"
#
# # List comprehension to extract words with more than 3 characters
# # 'text.split()' splits the string into a list of words
# # 'word' is each individual word in the list created by 'split()'
# # 'if len(word) > 3' filters only the words that have more than 3 characters
# long_words = [word for word in text.split() if len(word) > 3]
#
# # Print the list of words that have more than 3 characters
# print(long_words)
#
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = list1
#
# # Value equality
# print(list1 == list2)  # True: values are equal
# print(list1 == list3)  # True: values are equal
#
# # Reference equality
# print(list1 is list2)  # False: different objects
# print(list1 is list3)  # True: same object
