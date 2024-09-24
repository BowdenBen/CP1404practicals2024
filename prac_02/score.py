"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: ")) # Score variable holds input as a float
    while 0 <= score <= 100:  # while score is between 0-100 inclusive, loop continues to run
        result = score_check(score)
        print(result)

        # New part: Generate a random score and print the result
        random_score = random.randint(0, 100)  # Generates a random integer between 0 and 100
        print(f"\nRandom score: {random_score:.2f}")
        random_result = score_check(random_score)
        print(f"Result for random score: {random_result}\n")
        score = float(input("Enter score: "))  # Prompt for a new score inside the loop

    print("Invalid Score")


def score_check(score):
        if 90 <= score < 100:  # if, elif, else sets print conditions tied to variable score
            return "Excellent"
        elif 50 <= score < 90:
            return "Passable"
        else:
            return "Poor"



main()