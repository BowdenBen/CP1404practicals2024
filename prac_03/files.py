"""
Psuedo Code
Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.

In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
Use open and close for this question.

Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result, which should be... 59. Use with instead of open and close for this question.

Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers. Use with instead of open and close for this question.
"""

# Ask the user for their name
name = input("Enter your name: ")

# Open the file in write mode and write the name to it
file = open("name.txt", 'w')
file.write(name)

# Close the file
file.close()

# Open the file in read mode and read the name from it
file = open("name.txt", 'r')
name = file.read().strip()  # Use strip() to remove any extra newlines or spaces

# Close the file
file.close()

# Print the greeting
print(f"Hi {name}!")

# Open the file using 'with', which automatically closes the file after reading
with open("numbers.txt", 'r') as file:
    # Read the first two lines (numbers) and convert them to integers
    number1 = int(file.readline())
    number2 = int(file.readline())

# Add the two numbers and print the result
result = number1 + number2
print(result)  # This should print 59

