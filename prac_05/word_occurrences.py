"""
Word Occurrences
By Benjamin Bowden
Estimate: 30 minutes
Actual:   40 minutes
"""

# Prompt user for a string input and split the input string into a list of words
# The input() function captures the user's input, and split() divides the string into words using spaces as delimiters.
words = input("Enter a string: ").split()

# Initialize an empty dictionary to store word counts
# The dictionary will have words as keys and their counts as values.
word_count = {}

# Loop through each word in the list of words to count their occurrences
for word in words:
    # If the word is already in the dictionary (it has been encountered before)
    if word in word_count:
        # Increment the word's count by 1
        word_count[word] += 1
    else:
        # Otherwise, add the word to the dictionary with an initial count of 1
        word_count[word] = 1

# Sort the dictionary keys (the words) alphabetically
# sorted() returns a sorted list of keys from the word_count dictionary.
sorted_words = sorted(word_count.keys())

# Find the length of the longest word for proper formatting.
# max() finds the maximum length among all the words in word_count.
max_length = max(len(word) for word in word_count.keys())

# Loop through each word in the sorted list of words, Print the word counts with formatted output
for word in sorted_words:
    # Print each word and its corresponding count
    # f"{word:{max_length}}" ensures the words are left-aligned in a column, using the length of the longest word.
    print(f"{word:{max_length}} : {word_count[word]}")
