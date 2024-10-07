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

END
'''


def main():
    """Main function to input numbers and display information about them."""
    # Initialize an empty list to store the numbers
    numbers = []

    # Prompt the user to enter 5 numbers and add each to the list
    for i in range(5):
        # Get a number from the user, converting it to float (for decimal values)
        number = float(input(f"Number {i + 1}: "))
        # Add the entered number to the 'numbers' list
        numbers.append(number)

        # Output the requested information about the numbers
    print(f"The first number is {numbers[0]}")  # Display the first number in the list
    print(f"The last number is {numbers[-1]}")  # Display the last number in the list using negative indexing
    print(f"The smallest number is {min(numbers)}")  # Display the smallest number using the 'min' function
    print(f"The largest number is {max(numbers)}")  # Display the largest number using the 'max' function
    # Calculate and display the average of the numbers, formatted to 1 decimal place
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


# Call the main function to execute the program
main()
