

import random

def main():
    scores = int(input("How many random scores: ")) # Score variable holds input as a float

    while scores > 0:
        for i in range(scores):
            # New part: Generate a random score and print the result
            random_score = random.randint(0, 100)  # Generates a random integer between 0 and 100
            random_result = score_check(random_score)
            print(f"\nRandom score: {random_score:.2f} is {random_result}")
        scores = int(input("How many random scores: ")) # Score variable holds input as a float
    print("\nThank you for playing!")

def score_check(score):
        if 90 <= score < 100:  # if, elif, else sets print conditions tied to variable score
            return "Excellent"
        elif 50 <= score < 90:
            return "Passable"
        else:
            return "Poor"



main()