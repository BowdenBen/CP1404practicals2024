"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed
"""

# Store Menu in MENU constant
MENU = """(H)ello
(G)oodbye
(Q)uit"""
name = input("Enter your name: ") # Get name from user, store in name variable
print (MENU)
choice = input(">>> ").upper() # Get menu choice from user, store in choice variable, convert input to upper case
while choice != "Q": # While Q is not selected, run loop
    """ If, elif, else statement to deal with menu selection. """
    if choice == "H":
        print(f"Hello {name}")
        choice = input(">>> ").upper()
    elif choice == "G":
        print(f"Goodbye {name}")
        choice = input(">>> ").upper()
    else:
        print("Invalid input")
        choice = input(">>> ").upper()
print("Finished")
