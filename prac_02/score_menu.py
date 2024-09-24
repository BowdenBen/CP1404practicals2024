
# Define the menu options as a constant string.
MENU = "(G)et a valid score (must be 0-100 inclusive)\n" \
       "(P)rint result\n" \
       "(S)how stars\n" \
       "(Q)uit"

def main():
    """
    The main function to drive the program. It starts by initializing the score as None.
    Then it enters a loop where the user can choose an action from the menu.
    The program will keep looping until the user selects 'Q' to quit.
    """
    score = None  # Initialize score as None to track if a valid score has been entered
    choice = input(MENU + "\n>>> ").upper()  # Get the user's choice and convert it to uppercase
    while choice != "Q":  # Continue looping until the user chooses to quit
        if choice == "G":  # User selects to get a valid score
            score = get_valid_score()  # Call the function to get a valid score
        elif choice == "P":  # User selects to print the result
            if score is not None:  # Ensure a valid score exists before printing
                print_result(score)  # Call the function to print the result based on the score
            else:
                # If no score has been entered yet, inform the user
                print("No valid score entered yet. Please select 'G' to enter a score.")
        elif choice == "S":  # User selects to show stars
            if score is not None:  # Ensure a valid score exists before showing stars
                show_stars(score)  # Call the function to display stars
            else:
                # If no score has been entered yet, inform the user
                print("No valid score entered yet. Please select 'G' to enter a score.")
        else:
            # If the user enters an invalid menu option, display an error message
            print("Invalid choice. Please select from the menu options.")

        # After executing the selected option, re-prompt the user for another choice
        choice = input(MENU + "\n>>> ").upper()

    # If the user selects 'Q', display a farewell message and exit the loop
    print("Thank you for using the program. Goodbye!")

def get_valid_score():
    """
    Prompts the user to enter a valid score between 0 and 100 inclusive.
    The function validates the input to ensure it is a number within the correct range.
    If the input is invalid, the user is prompted again.

    Returns:
        score (int): A valid score between 0 and 100 inclusive.
    """
    score = -1  # Initialize with an invalid score to enter the loop
    while not (0 <= score <= 100):  # Loop until a valid score is entered
        try:
            # Prompt the user to enter a score
            score = int(input("Please enter a score (0-100): "))
            if not (0 <= score <= 100):
                # If the score is not within the valid range, display an error message
                print("Invalid score; must be between 0 and 100.")
        except ValueError:
            # If the input is not a valid integer, display an error message
            print("Invalid input; please enter a number.")
    return score  # Return the valid score once entered

def print_result(score):
    """
    Determines and prints the result based on the score.
    The result is categorized into 'Excellent', 'Passable', or 'Poor' based on the score.

    Args:
        score (int): The score entered by the user.
    """
    # Check the score and print the corresponding result
    if 90 <= score <= 100:
        print("Your result is: Excellent")
    elif 50 <= score < 90:
        print("Your result is: Passable")
    else:
        print("Your result is: Poor")

def show_stars(score):
    """
    Displays stars equal to the integer part of the score.
    If the score is 85, the program will print 85 stars.

    Args:
        score (int): The score entered by the user.
    """
    # Print a line of stars equal to the score
    print("*" * int(score))

# Call the main function to run the program
if __name__ == "__main__":
    main()  # The main function starts the program
