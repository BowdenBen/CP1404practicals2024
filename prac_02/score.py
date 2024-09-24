"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: ")) # Score variable holds input as a float
while 0 <= score <= 100: # while score is between 0-100 inclusive, loop continues to run
    if 90 <= score < 100: # if, elif, else sets print conditions tied to variable score
        print("Excellent")
    elif 50 <= score < 90:
        print("Passable")
    else :
        print("Poor")
    score = float(input("Enter score: ")) # loop continues for next user input
print("Invalid Score")