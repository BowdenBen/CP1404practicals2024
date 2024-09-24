"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: ")) # Score variable holds input as a float
    result = score_check(score)
    print(result)


def score_check(score):
    while 0 <= score <= 100:  # while score is between 0-100 inclusive, loop continues to run
        if 90 <= score < 100:  # if, elif, else sets print conditions tied to variable score
            return "Excellent"
        elif 50 <= score < 90:
            return "Passable"
        else:
            return "Poor"
    print("Invalid Score")


main()