import random  # Import the random module to generate random numbers


def main():
    """
    Main function to generate random scores and evaluate them.
    """
    # Prompt the user to input the number of random scores to generate
    scores = int(input("How many random scores: "))  # 'scores' variable holds input as an integer

    while scores > 0:
        # Loop to generate and evaluate the specified number of random scores
        for i in range(scores):
            # Generate a random score between 0 and 100 (inclusive)
            random_score = random.randint(0, 100)
            # Evaluate the random score using the score_check function
            random_result = score_check(random_score)
            # Print the random score and its evaluation
            print(f"\nRandom score: {random_score} is {random_result}")
        # After generating the scores, prompt the user again
        scores = int(input("How many random scores: "))  # Prompt for a new number of random scores
    # When the loop ends (user enters 0 or negative number), print a goodbye message
    print("\nThank you for playing!")


def score_check(score):
    """
    Function to evaluate the score and return a corresponding performance string.

    Parameters:
    score (int): The score to evaluate.

    Returns:
    str: The performance evaluation ('Excellent', 'Passable', or 'Poor').
    """
    if 90 <= score <= 100:  # Check if the score is between 90 and 100 inclusive
        return "Excellent"
    elif 50 <= score < 90:  # Check if the score is between 50 and 89 inclusive
        return "Passable"
    else:
        return "Poor"  # If the score is below 50, return 'Poor'


# Call the main function to execute the program
main()
