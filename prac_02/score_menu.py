


MENU = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    score = None  # Initialize score as None to track if a valid score has been entered
    choice = input(MENU + "\n>>> ").upper()  # Get user's choice
    while choice != "Q":  # Continue looping until user chooses to quit
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score is not None:
                print_result(score)
            else:
                print("No valid score entered yet. Please select 'G' to enter a score.")
        elif choice == "S":
            if score is not None:
                show_stars(score)
            else:
                print("No valid score entered yet. Please select 'G' to enter a score.")
        else:
            print("Invalid choice. Please select from the menu options.")
        choice = input(MENU + "\n>>> ").upper()  # Re-prompt for choice
    print("Thank you for using the program. Goodbye!")  # Farewell message

def get_valid_score():
    """Prompt the user for a valid score between 0 and 100 inclusive."""
    score = -1  # Initialize with an invalid score to enter the loop
    while not (0 <= score <= 100):  # Loop until a valid score is entered
        try:
            score = int(input("Please enter a score (0-100): "))
            if not (0 <= score <= 100):
                print("Invalid score; must be between 0 and 100.")
        except ValueError:  # Error checking for integer
            print("Invalid input; please enter a number.")
    return score

def print_result(score):
    """Determine and print the result based on the score."""
    if 90 <= score <= 100:
        print("Your result is: Excellent")
    elif 50 <= score < 90:
        print("Your result is: Passable")
    else:
        print("Your result is: Poor")

def show_stars(score):
    """Display stars equal to the integer part of the score."""
    print("*" * int(score))

# Call the main function to run the program
main()