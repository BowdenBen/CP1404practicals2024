import random  # Import the random module to use for generating random numbers

def main():
    """
    Main function to interact with the user, evaluate their entered score,
    generate a random score, and display the results.
    """
    # Prompt the user to enter a score and convert the input to a float
    score = float(input("Enter score: "))  # Score variable holds input as a float

    # Continue looping as long as the score is between 0 and 100 inclusive
    while 0 <= score <= 100:  # While score is between 0-100 inclusive, loop continues to run
        # Call the score_check function to evaluate the user's score
        result = score_check(score)
        # Print the evaluation result for the user's score
        print(result)

        # New part: Generate a random score and print the result
        random_score = random.randint(0, 100)  # Generates a random integer between 0 and 100
        # Print the random score formatted to two decimal places
        print(f"\nRandom score: {random_score:.2f}")
        # Call the score_check function to evaluate the random score
        random_result = score_check(random_score)
        # Print the evaluation result for the random score
        print(f"Result for random score: {random_result}\n")
        # Prompt the user to enter another score and convert it to a float
        score = float(input("Enter score: "))  # Prompt for a new score inside the loop

    # If the entered score is not between 0 and 100, print "Invalid Score"
    print("Invalid Score")


def score_check(score):
    """
    Function to evaluate the score and return a corresponding performance string.

    Parameters:
    score (float): The score to evaluate.

    Returns:
    str: The performance evaluation ('Excellent', 'Passable', or 'Poor').
    """
    if 90 <= score < 100:  # If score is between 90 (inclusive) and less than 100
        return "Excellent"
    elif 50 <= score < 90:  # If score is between 50 (inclusive) and less than 90
        return "Passable"
    else:
        return "Poor"  # If score is less than 50 or greater than or equal to 100

# Call the main function to execute the program
main()
