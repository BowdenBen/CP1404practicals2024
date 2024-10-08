'''
START

    CREATE an empty list called numbers

    FOR each number from 1 to 5:
        PROMPT the user to input a number
        CONVERT the input to a floating-point number
        ADD the number to the numbers list

    DISPLAY "The first number is" followed by the first element of the numbers list
    DISPLAY "The last number is" followed by the last element of the numbers list
    DISPLAY "The smallest number is" followed by the smallest element in the numbers list
    DISPLAY "The largest number is" followed by the largest element in the numbers list
    CALCULATE the average by dividing the sum of the numbers list by the number of elements in the list
    DISPLAY "The average of the numbers is" followed by the calculated average

    Copy the following list of usernames:

   usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
   'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
Ask the user for their username. If the username is in the above list of authorised users, print "Access granted",
otherwise print "Access denied".



END
'''


def main():
    """Main function to input numbers, display information, and check user access."""

    # Initialize an empty list to store the numbers that the user will input
    numbers = []

    # List of authorized usernames for access control
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    # Prompt the user to enter 5 numbers and add each to the list
    for i in range(5):
        # Get a number from the user, convert it to a float to allow decimal values
        number = float(input(f"Number {i + 1}: "))
        # Add the entered number to the 'numbers' list using append
        numbers.append(number)

    # Output the requested information about the numbers
    print(f"The first number is {numbers[0]}")  # Display the first number in the list (index 0)
    print(f"The last number is {numbers[-1]}")  # Display the last number in the list (negative index -1)
    print(f"The smallest number is {min(numbers)}")  # Display the smallest number using the 'min' function
    print(f"The largest number is {max(numbers)}")  # Display the largest number using the 'max' function
    # Calculate and display the average of the numbers using sum and len, formatted to 1 decimal place
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

    # Prompt the user to enter their username for access control
    username = input("Enter your username: ")

    # Check if the entered username is in the list of authorized users
    if username in usernames:
        print("Access granted")  # If the username exists in the list, grant access
    else:
        print("Access denied")  # If the username is not in the list, deny access


# Call the main function to execute the program
main()

