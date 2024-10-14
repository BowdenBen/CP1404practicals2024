"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Dictionary of Australian state/territory codes and their full names.
# The keys are state abbreviations (like 'QLD') and the values are the corresponding full names (like 'Queensland').
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# Print the entire dictionary for initial reference.
# This displays all state codes and their respective names.
print(CODE_TO_NAME)

# Loop through the dictionary and print each state code and full name, formatted in a neat, aligned manner.
# The f-string formatting ensures that the state code is left-aligned in a field of width 3.
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

# Input and process state codes using EAFP
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        # If the state code exists in CODE_TO_NAME, this will succeed, and the state's name is printed.
        print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        # If the state code doesn't exist in the dictionary, a KeyError is raised.
        # The KeyError is caught and an error message is displayed to the user.
        print("Invalid short state")
    # After processing, ask the user for another state code.
    # The input is again converted to uppercase to maintain case-insensitivity.
    state_code = input("Enter short state: ").upper()
