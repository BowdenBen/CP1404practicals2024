"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False # Use boolean to set variable so loop can be entered
while not is_finished: # while loop based on boolean
    try:
        # Attempt to get a valid integer from the user
        result = int(input("Enter a valid integer: "))
        is_finished = True # this finishes the loop if an integer is entered
    except ValueError: # ValueError catches anything tha is not an integer
        print("Please enter a valid integer.")
# Output the valid integer once it has been successfully entered
print("Valid result is:", result)
