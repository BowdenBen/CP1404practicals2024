'''
PseudoCode
START

    DEFINE constant MIN_NUMBER = 1
    DEFINE constant MAX_NUMBER = 45
    DEFINE constant NUMBERS_PER_PICK = 6

    PROMPT user for the number of quick picks (store in variable quick_picks)

    FOR each quick pick from 1 to quick_picks:
        CREATE an empty list called current_pick to store numbers

        WHILE length of current_pick is less than NUMBERS_PER_PICK:
            GENERATE a random number between MIN_NUMBER and MAX_NUMBER
            IF random number is not already in current_pick:
                ADD the random number to current_pick

        SORT the current_pick list in ascending order
        FORMAT and DISPLAY the numbers in current_pick with 2 spaces between each number

END

'''

import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Main function to generate and display the quick picks"""
    quick_picks = int(input("How many quick picks? ")) # Ask the user for the number of quick picks they wish to generate

    for i in range(quick_picks): # Loop for the number of quick picks the user requested
        current_pick = [] # Initialize an empty list to hold the numbers

        while len(current_pick) < NUMBERS_PER_PICK: # Generate numbers for each quick pick up to NUMBERS_PER_PICK
            number = random.randint(MIN_NUMBER, MAX_NUMBER) # Numbers generated are between 2 boundaries
            if number not in current_pick: # Check for double ups
                current_pick.append(number) # Add number to list

        current_pick.sort() # Sort each quick pick from low to high


        print(" ".join(f"{num:2}" for num in current_pick)) # Print each quick pick


main()
