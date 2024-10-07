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

