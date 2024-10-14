"""
Word Occurrences
By Benjamin Bowden
Estimate: 20 minutes
Actual:   32 minutes
"""


# Prompt user for a string input
input_string = input("Enter a string: ")

# Split the input string into words
words = input_string.split()

# Initialize an empty dictionary to store word counts
word_count = {}

# Loop through each word in the list of words
for word in words:
    # If the word is already in the dictionary
    if word in word_count:
        # Increment the word's count
        word_count[word] += 1
    else:
        # Otherwise, add the word to the dictionary with a count of 1
        word_count[word] = 1

print(word_count)

# Find the length of the longest word for formatting
max_length = find the length of the longest word in word_count.keys()

# Sort the dictionary by word (key) alphabetically
sorted_words = sorted(word_count.keys())

# Print the word counts with formatted output
for each word in sorted_words:
    # Print word and its count, aligned using f-string formatting
    print(f"{word:{max_length}} : {word_count[word]}")

# End of function
